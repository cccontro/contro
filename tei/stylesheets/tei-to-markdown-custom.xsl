<!--
Stylesheet for converting TEI to HTML-in-Markdown format, intended for post-processing
with Python-Markdown.

It links to the official TEI Stylesheets repo: to use it you must clone the contro repo
with the option `git clone recurse-submodules` (double hyphen before recurse-submodules)
so as to initialize it.
-->

<xsl:stylesheet
        version="3.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        xmlns:tei="http://www.tei-c.org/ns/1.0"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xpath-default-namespace="http://www.tei-c.org/ns/1.0"
        exclude-result-prefixes="tei xs">

    <xsl:import href="official/common/common.xsl" />


    <doc xmlns="http://www.oxygenxml.com/ns/doc/xsl" scope="stylesheet" type="stylesheet">
        <desc>

            <p>This software is dual-licensed:

                1. Distributed under a Creative Commons Attribution-ShareAlike 3.0
                Unported License http://creativecommons.org/licenses/by-sa/3.0/

                2. http://www.opensource.org/licenses/BSD-2-Clause


                Redistribution and use in source and binary forms, with or without
                modification, are permitted provided that the following conditions are
                met:

                * Redistributions of source code must retain the above copyright
                notice, this list of conditions and the following disclaimer.

                * Redistributions in binary form must reproduce the above copyright
                notice, this list of conditions and the following disclaimer in the
                documentation and/or other materials provided with the distribution.

                This software is provided by the copyright holders and contributors
                "as is" and any express or implied warranties, including, but not
                limited to, the implied warranties of merchantability and fitness for
                a particular purpose are disclaimed. In no event shall the copyright
                holder or contributors be liable for any direct, indirect, incidental,
                special, exemplary, or consequential damages (including, but not
                limited to, procurement of substitute goods or services; loss of use,
                data, or profits; or business interruption) however caused and on any
                theory of liability, whether in contract, strict liability, or tort
                (including negligence or otherwise) arising in any way out of the use
                of this software, even if advised of the possibility of such damage.
            </p>
            <p>Author: See AUTHORS</p>

            <p>Copyright: 2013, TEI Consortium</p>
        </desc>
    </doc>

    <xsl:output method="xhtml" html-version="5.0" encoding="UTF-8" indent="no" omit-xml-declaration="yes" />

    <!-- Hide either of the two languages -->
    <xsl:param name="lang" as="xs:string" required="no" select="'it'" />
    <xsl:template match="*[@xml:lang= $lang]" priority="10" />

    <!-- Suffix for the opposite language -->
    <xsl:variable name="other-lang" as="xs:string" select="if ($lang = 'it') then 'en' else 'it'" />

    <!-- Match only titles, character list and text, avoid all other metadata -->
    <xsl:template match="/">
        <xsl:apply-templates select="//titleStmt" />
        <xsl:call-template name="newline" />
        <xsl:call-template name="newline" />
        <xsl:apply-templates select="//particDesc" />
        <xsl:apply-templates select="//text" />
    </xsl:template>

    <!-- HTML-in-markdown -->

    <!-- Base templates -->
    <xsl:template name="makeBlock">
        <xsl:param name="style" />
        <xsl:param name="title" select="()" />
        <xsl:param name="element" select="()" />

        <xsl:call-template name="newline" />
        <xsl:element name="{if ($element) then $element else 'div'}">
            <xsl:attribute name="markdown">1</xsl:attribute>
            <xsl:attribute name="class">
                <xsl:value-of select="name()" />
                <xsl:text xml:space="preserve"> </xsl:text>
                <xsl:value-of select="@type" />
            </xsl:attribute>
            <xsl:if test="@xml:id">
                <xsl:attribute name="id">
                    <xsl:value-of select="@xml:id" />
                </xsl:attribute>
            </xsl:if>
            <xsl:if test="@ana">
                <xsl:attribute name="ana">
                    <xsl:value-of select="@ana" />
                </xsl:attribute>
            </xsl:if>
            <xsl:if test="$title">
                <xsl:attribute name="title">
                    <xsl:value-of select="$title" />
                </xsl:attribute>
            </xsl:if>
            <xsl:call-template name="newline" />
            <xsl:apply-templates />
        </xsl:element>
        <xsl:call-template name="newline" />
    </xsl:template>

    <xsl:template name="makeSpan">
        <xsl:element name="span">
            <xsl:attribute name="markdown">1</xsl:attribute>
            <xsl:if test="@xml:id">
                <xsl:attribute name="id">
                    <xsl:value-of select="if (ends-with(@xml:id, '-it') or ends-with(@xml:id, '-en'))
                                          then @xml:id
                                          else concat(@xml:id, '-', $other-lang)" />
                </xsl:attribute>
            </xsl:if>
            <xsl:if test="@ana">
                <xsl:attribute name="ana">
                    <xsl:value-of select="@ana" />
                </xsl:attribute>
                <xsl:variable name="target" select="id(substring(@ana, 2))" />
                <xsl:if test="$target/catDesc">
                    <xsl:attribute name="title">
                        <xsl:value-of disable-output-escaping="yes" select="string-join($target/catDesc, '.&lt;br/&gt;')" />
                    </xsl:attribute>
                </xsl:if>
            </xsl:if>
            <xsl:apply-templates />
        </xsl:element>
    </xsl:template>

    <xsl:template name="makeInline">
        <xsl:param name="before" />
        <xsl:param name="style" />
        <xsl:param name="after" />
    </xsl:template>

    <xsl:template match="list|note">
        <xsl:call-template name="newline" />
        <xsl:call-template name="makeBlock" />
        <xsl:call-template name="newline" />
    </xsl:template>

    <!-- Analysis reference as attribute in a div/span -->
    <xsl:template match="*[@ana]">
        <xsl:choose>
            <xsl:when test="tei:isInline(.)">
                <xsl:call-template name="makeSpan" />
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="makeBlock">
                    <xsl:with-param name="element" select="if (name() = 'p') then 'p' else 'div'" />
                </xsl:call-template>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- Block quotes -->
    <xsl:template match="quote">
        <xsl:call-template name="makeBlock">
            <xsl:with-param name="element" select="'blockquote'" />
            <xsl:with-param name="title" select="parent::cit/bibl" />
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="bibl" />

    <!-- Markdown -->

    <!-- Base templates -->
    <xsl:template match="gap">
        <xsl:text>[...]</xsl:text>
    </xsl:template>

    <xsl:template match="hi[@rend = 'bold']">
        <xsl:text>**</xsl:text>
        <xsl:apply-templates />
        <xsl:text>**</xsl:text>
    </xsl:template>

    <xsl:template match="foreign">
        <xsl:text xml:space="preserve">*</xsl:text>
        <xsl:apply-templates />
        <xsl:text xml:space="preserve">*</xsl:text>
    </xsl:template>

    <xsl:template match="mentioned">
        <xsl:text>“</xsl:text>
        <xsl:apply-templates />
        <xsl:text>”</xsl:text>
    </xsl:template>

    <xsl:template match="p|trailer">
        <xsl:call-template name="newline" />
        <xsl:apply-templates />
        <xsl:call-template name="newline" />
    </xsl:template>

    <xsl:template match="label">
        <xsl:apply-templates />
    </xsl:template>

    <!-- Main title -->
    <xsl:template match="titleStmt">
        <xsl:apply-templates select="title[@type = 'main' and @xml:lang!= $lang]" mode="main"/>
        <xsl:apply-templates select="title[@type = 'sub']" />
    </xsl:template>


    <xsl:template match="title" mode="main">
        <xsl:text xml:space="preserve">## </xsl:text>
        <xsl:apply-templates />
        <xsl:text xml:space="preserve"> {: #</xsl:text>
        <xsl:value-of select="substring-before(., ' ')" />
        <xsl:text xml:space="preserve"> data-toc-label="</xsl:text>
        <xsl:value-of select="substring-before(., ' ')" />
        <xsl:text xml:space="preserve">" }&#10;</xsl:text>
    </xsl:template>

    <xsl:template match="title">
        <xsl:apply-templates />
    </xsl:template>

    <!-- Subtitles smaller and on new line -->
    <xsl:template match="title[@type = 'sub']">
        <xsl:call-template name="newline" />
        <p class="subtitle" markdown="span">
            <xsl:apply-templates />
        </p>
    </xsl:template>

    <!-- Inline notes -->
    <xsl:template match="note[@place = 'inline']">
        <xsl:text>[</xsl:text>
        <xsl:apply-templates />
        <xsl:text>]</xsl:text>
    </xsl:template>

    <!-- Poetry -->
    <xsl:template match="*[@rendition = 'expandable']" priority="2">
        <details markdown="block">
            <summary></summary>
            <xsl:call-template name="newline" />
            <xsl:apply-templates />
            <xsl:call-template name="newline" />
        </details>
    </xsl:template>

    <xsl:template match="lg">
        <xsl:if test="@n">
            <xsl:value-of select="@n" />
            <xsl:text xml:space="preserve">.  </xsl:text>
        </xsl:if>
        <xsl:call-template name="newline" />
        <xsl:apply-templates />
        <xsl:call-template name="newline" />
    </xsl:template>

    <xsl:template match="l">
        <xsl:choose>
            <xsl:when test="@n">
                <xsl:text xml:space="preserve">    </xsl:text>
                <xsl:number value="@n" format="1." />
                <xsl:text xml:space="preserve">  </xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="newline" />
            </xsl:otherwise>
        </xsl:choose>
        <xsl:apply-templates />
        <xsl:call-template name="newline" />
    </xsl:template>

    <!-- Character to reference list -->
    <xsl:template match="person">
        <xsl:value-of select="tei:mkRef(@xml:id,@sameAs,persName)" />
        <xsl:call-template name="newline" />
        <xsl:apply-templates select="persona" />
    </xsl:template>

    <xsl:template match="persona">
        <xsl:value-of disable-output-escaping="yes" select="tei:mkRef(@xml:id, parent::person/@sameAs, concat(persName, ' (', parent::person/persName, ').', tei:tag('br', 'open-close'), note))" />
        <xsl:call-template name="newline" />
    </xsl:template>

    <!-- Markdown link in regular or reference syntax -->
    <xsl:function name="tei:mkLink">
        <xsl:param name="content" />
        <xsl:param name="target" />
        <xsl:param name="syntax" />

        <xsl:text>[</xsl:text>
        <xsl:value-of select="$content" />

        <xsl:choose>
            <xsl:when test="$syntax = 'reference'">
                <xsl:text>][</xsl:text>
                <xsl:value-of select="$target" />
                <xsl:text>]</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>](</xsl:text>
                <xsl:value-of select="$target" />
                <xsl:text>)</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:function>

    <!-- Markdown reference -->
    <xsl:function name="tei:mkRef">
        <xsl:param name="content" />
        <xsl:param name="target" />
        <xsl:param name="title" />

        <xsl:text>[</xsl:text>
        <xsl:value-of select="$content" />
        <xsl:text xml:space="preserve">]: </xsl:text>
        <xsl:value-of select="$target" />
        <xsl:if test="exists($title)">
            <xsl:text xml:space="preserve"> "</xsl:text>
            <xsl:value-of select="$title" />
            <xsl:text>"</xsl:text>
        </xsl:if>
    </xsl:function>

    <!-- Add id, class and/or title to a markdown link -->
    <xsl:template name="mkLinkAttrs">
        <xsl:param name="id" select="()" />
        <xsl:param name="class" select="()" />
        <xsl:param name="title" select="()" />
        <xsl:param name="ana" select="()" />
        <xsl:param name="against" select="()" />
        <xsl:param name="label" select="()" />

        <xsl:text>{:</xsl:text>
        <xsl:if test="exists($id)">
            <xsl:text xml:space="preserve"> #</xsl:text>
            <xsl:value-of select="$id" />
            <xsl:text xml:space="preserve"> label="</xsl:text>
            <xsl:value-of select="$id" />
            <xsl:text>"</xsl:text>
        </xsl:if>
        <xsl:if test="exists($class)">
            <xsl:text xml:space="preserve"> .</xsl:text>
            <xsl:value-of select="$class" />
        </xsl:if>
        <xsl:if test="exists($title)">
            <xsl:text xml:space="preserve"> title="</xsl:text>
            <xsl:value-of disable-output-escaping="yes" select="$title" />
            <xsl:text>"</xsl:text>
        </xsl:if>
        <xsl:if test="exists($ana)">
            <xsl:text xml:space="preserve"> ana="</xsl:text>
            <xsl:value-of disable-output-escaping="yes" select="$ana" />
            <xsl:text>"</xsl:text>
        </xsl:if>
        <xsl:if test="exists($against)">
            <xsl:text xml:space="preserve"> against="</xsl:text>
            <xsl:value-of disable-output-escaping="yes" select="substring($against, 2)" />
            <xsl:text>"</xsl:text>
        </xsl:if>
        <xsl:if test="exists($label)">
            <xsl:text xml:space="preserve"> label="</xsl:text>
            <xsl:value-of select="$label" />
            <xsl:text>"</xsl:text>
        </xsl:if>
        <xsl:text xml:space="preserve"> }</xsl:text>
    </xsl:template>

    <!-- Links to external resources are rendered in markdown reference syntax -->
    <xsl:template match="*[@ref]">
        <xsl:value-of select="tei:mkLink(.,substring(@ref, 2),'reference')" />
    </xsl:template>

    <!-- Pointers are rendered as regular markdown links with the text content of the target -->
    <xsl:template match="ptr">
        <xsl:variable name="target-id" select="substring(@target, 2)" />
        <xsl:variable name="target-text" select="id($target-id)" />

    <xsl:variable name="target-element" select="//*[@xml:id=$target-id]" />
    <xsl:variable name="exclude-id" select="$target-element/@exclude" />

        <xsl:value-of select="tei:mkLink($target-text,@target,'')" />
        <xsl:call-template name="mkLinkAttrs">
            <xsl:with-param name="class" select="'ref'" />
            <xsl:with-param name="label" select="$target-id" />
            <xsl:with-param name="against" select="$exclude-id" />
        </xsl:call-template>
    </xsl:template>

    <!-- In-line quotes call the link template if a corresp id is given -->
    <xsl:template match="q" priority="2">
        <xsl:text>«</xsl:text>
        <xsl:if test="@type = 'foreign'">
            <xsl:text>*</xsl:text>
        </xsl:if>
        <xsl:choose>
            <xsl:when test="@corresp">
                <xsl:call-template name="corresp" />
            </xsl:when>
            <xsl:when test="parent::cit">
                <xsl:element name="span">
                    <xsl:attribute name="title">
                        <xsl:value-of select="parent::cit/bibl" />
                    </xsl:attribute>
                    <xsl:attribute name="class" select="'q'" />
                    <xsl:apply-templates />
                </xsl:element>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates />
            </xsl:otherwise>
        </xsl:choose>
        <xsl:if test="@type = 'foreign'">
            <xsl:text>*</xsl:text>
        </xsl:if>
        <xsl:text>»</xsl:text>
    </xsl:template>

    <!-- In-text references are rendered as regular markdown links.
         The title is set as the location of the referent, if available. -->
    <xsl:template match="*[@corresp]" name="corresp">
        <xsl:variable name="corresp-suffixed"
              select="if (ends-with(@corresp, '-it') or ends-with(@corresp, '-en'))
                      then @corresp
                      else concat(@corresp, '-', $other-lang)" />
        <xsl:value-of select="tei:mkLink(.,$corresp-suffixed,'')" />
        <xsl:variable name="target" select="id(substring(@corresp, 2))" />
        <xsl:choose>
            <xsl:when test="$target/parent::l">
                <xsl:call-template name="mkLinkAttrs">
                    <xsl:with-param name="class" select="name()" />
                    <xsl:with-param name="title" select="tei:poemRef($target)" />
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="mkLinkAttrs">
                    <xsl:with-param name="class" select="name()" />
                    <xsl:with-param name="title" select="tei:proseRef($target)" />
                </xsl:call-template>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- Prose references are rendered as title, optional section, page number -->
    <xsl:function name="tei:proseRef">
        <xsl:param name="target" />

        <xsl:variable name="ancestor" select="outermost($target/ancestor::div)" />
        <xsl:variable name="title" select="concat(tei:tag('em','open'), $ancestor//title[not(@type = 'sub' or @xml:lang = $lang)], tei:tag('em','close'))" />
        <xsl:variable name="section" select="concat(' ',$target/ancestor::div[1]/@n)" />

        <xsl:choose>
            <xsl:when test="$ancestor/@n">
                <xsl:value-of select="concat($title, $section, ', p. ', $ancestor/@n)" />
            </xsl:when>
            <xsl:when test="$ancestor/@from">
                <xsl:value-of select="concat($title, $section, ', pp. ', $ancestor/@from, '–', $ancestor/@from)" />
            </xsl:when>
        </xsl:choose>
    </xsl:function>

    <!-- Poetic references are rendered as first line of poem + stanza and line numbers -->
    <xsl:function name="tei:poemRef">
        <xsl:param name="target" />

        <xsl:variable name="title" select="string-join(tei:poemTitle($target))" />
        <xsl:variable name="sections" select="string-join($target/ancestor::lg/@n, ', ')" />

        <xsl:value-of select="concat($title, ' ', $sections, ', ', $target/parent::l/@n)" />
    </xsl:function>

    <xsl:function name="tei:poemTitle">
        <xsl:param name="target" />
        <xsl:variable name="poem" select="outermost($target/ancestor::lg)" />
        <xsl:variable name="opening" select="head($poem//l[1])" />
        
        <xsl:value-of disable-output-escaping="yes" select="tei:tag('em','open')" />
        <xsl:value-of select="replace($opening, '[\p{P}\s]+$', '')" /> <!-- Strip punctuation marks -->
        <xsl:value-of select="tei:tag('em','close')" />
    </xsl:function>

    <!-- Helper function to insert escaped tags inside markdown titles -->
    <xsl:function name="tei:tag">
        <xsl:param name="element" />
        <xsl:param name="mode" />

        <xsl:choose>
            <xsl:when test="$mode = 'open'">
                <xsl:value-of select="concat('&lt;',$element,'&gt;')" />
            </xsl:when>
            <xsl:when test="$mode = 'close'">
                <xsl:value-of select="concat('&lt;/',$element,'&gt;')" />
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="concat('&lt;',$element,'/&gt;')" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:function>

    <!-- Headers -->
    <xsl:template match="head">
        <xsl:variable name="depth">
            <xsl:apply-templates mode="depth" select=".." />
        </xsl:variable>
        <xsl:call-template name="newline" />
        <xsl:choose>
            <xsl:when test="$depth=0">###</xsl:when>
            <xsl:when test="$depth=1">####</xsl:when>
            <xsl:when test="$depth=2">#####</xsl:when>
            <xsl:when test="$depth=3">######</xsl:when>
            <xsl:otherwise>#</xsl:otherwise>
        </xsl:choose>
        <xsl:text xml:space="preserve"> </xsl:text>
        <xsl:apply-templates select="title" />
        <xsl:apply-templates select="text()" />
        <xsl:call-template name="newline" />
        <xsl:if test="parent::div/@resp">
            <xsl:variable name="resp" select="substring(parent::div/@resp, 2)" />
            <xsl:variable name="target" select="id($resp)" />

            <xsl:variable name="title" select="
                if (name($target) = 'persona') 
                then concat($target/persName, ' (', $target/parent::person/persName, ')')
                else $target/persName" />

            <xsl:value-of select="tei:mkLink($title, $resp, 'reference')" />

            <xsl:call-template name="newline" />
            <xsl:call-template name="newline" />
        </xsl:if>
    </xsl:template>

    <!-- Lists -->
    <xsl:template match="item" priority="2">
        <xsl:call-template name="newline" />
        <xsl:choose>
            <xsl:when test="tei:isOrderedList(..)">
                <xsl:number format="1." />
                <xsl:text xml:space="preserve">  </xsl:text>
                <xsl:call-template name="itemAttrs" />
                <xsl:call-template name="newline" />
            </xsl:when>
            <xsl:when test="parent::list[@type='gloss']">
                <xsl:text xml:space="preserve">:  </xsl:text>
                <xsl:call-template name="itemAttrs" />
                <xsl:call-template name="newline" />
                <xsl:call-template name="newline" />
            </xsl:when>
            <xsl:otherwise>
                <xsl:text xml:space="preserve">*  </xsl:text>
                <xsl:call-template name="itemAttrs" />
                <xsl:call-template name="newline" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template name="itemAttrs">
        <xsl:apply-templates />
        <xsl:if test="@xml:id|@ana">
            <xsl:call-template name="newline" />
            <xsl:call-template name="mkLinkAttrs">
                <xsl:with-param name="id" select="@xml:id" />
                <xsl:with-param name="ana" select="@ana" />
                <xsl:with-param name="against" select="@exclude" />
            </xsl:call-template>
        </xsl:if>
    </xsl:template>

    <!-- Helper templates -->
    <xsl:template name="newline">
        <xsl:text>&#10;</xsl:text>
    </xsl:template>

    <xsl:template name="horizontalRule">
        <xsl:text>&#10;---&#10;</xsl:text>
    </xsl:template>

    <xsl:template name="generateEndLink">
        <xsl:param name="where" />
    </xsl:template>

    <xsl:template name="emphasize">
        <xsl:param name="class" />
        <xsl:param name="content" />
        <xsl:choose>
            <xsl:when test="$class='titlem'">
                <xsl:text>_</xsl:text>
                <xsl:copy-of select="$content" />
                <xsl:text>_</xsl:text>
            </xsl:when>
            <xsl:when test="$class='titlej'">
                <xsl:text>_</xsl:text>
                <xsl:copy-of select="$content" />
                <xsl:text>_</xsl:text>
            </xsl:when>
            <xsl:when test="$class='titlea'">
                <xsl:text>‘</xsl:text>
                <xsl:copy-of select="$content" />
                <xsl:text>’</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:copy-of select="$content" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

</xsl:stylesheet>
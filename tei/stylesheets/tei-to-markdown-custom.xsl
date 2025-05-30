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

    <xsl:strip-space elements="additional address adminInfo
                altGrp altIdentifier analytic
                app appInfo application
                arc argument attDef
                attList availability back
                biblFull biblStruct bicond
                binding bindingDesc body
                broadcast cRefPattern calendar
                calendarDesc castGroup
                castList category certainty
                char charDecl charProp
                choice cit classDecl
                classSpec classes climate
                cond constraintSpec correction
                custodialHist decoDesc
                dimensions div div1 div2
                div3 div4 div5 div6
                div7 divGen docTitle eLeaf
                eTree editionStmt
                editorialDecl elementSpec
                encodingDesc entry epigraph
                epilogue equipment event
                exemplum fDecl fLib
                facsimile figure fileDesc
                floatingText forest front
                fs fsConstraints fsDecl
                fsdDecl fvLib gap glyph
                graph graphic group
                handDesc handNotes history
                hom hyphenation iNode if
                imprint incident index
                interpGrp interpretation join
                joinGrp keywords kinesic
                langKnowledge langUsage
                layoutDesc leaf lg linkGrp
                list listBibl listChange
                listEvent listForest listNym
                listOrg listPerson listPlace
                listRef listRelation
                listTranspose listWit location
                locusGrp macroSpec metDecl
                moduleRef moduleSpec monogr
                msContents msDesc msIdentifier
                msItem msItemStruct msPart
                namespace node normalization
                notatedMusic notesStmt nym
                objectDesc org particDesc
                performance person personGrp
                physDesc place population
                postscript precision
                profileDesc projectDesc
                prologue publicationStmt
                quotation rdgGrp recordHist
                recording recordingStmt
                refsDecl relatedItem relation
                relationGrp remarks respStmt
                respons revisionDesc root
                row samplingDecl schemaSpec
                scriptDesc scriptStmt seal
                sealDesc segmentation
                seriesStmt set setting
                settingDesc sourceDesc
                sourceDoc sp spGrp space
                spanGrp specGrp specList
                state stdVals subst
                substJoin superEntry
                supportDesc surface surfaceGrp
                table tagsDecl taxonomy
                teiCorpus teiHeader terrain
                text textClass textDesc
                timeline titlePage titleStmt
                trait transpose tree
                triangle typeDesc vAlt
                vColl vDefault vLabel
                vMerge vNot vRange valItem
                valList vocal" />

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
        <xsl:apply-templates select="//particDesc" />
        <xsl:apply-templates select="//text" />
    </xsl:template>

    <!-- HTML-in-markdown -->

    <!-- Base templates -->
    <xsl:template name="makeBlock">
        <xsl:param name="style" />
        <xsl:param name="element" />

        <xsl:call-template name="newline" />
        <xsl:element name="{if ($element = 'p') then 'p' else 'div'}">
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

    <!-- Main title rendered without anchor link -->
    <xsl:template match="titleStmt">
        <h1>
            <xsl:apply-templates select="title" />
        </h1>
        <xsl:call-template name="newline" />
    </xsl:template>

    <xsl:template match="title">
        <xsl:value-of select="." />
    </xsl:template>

    <!-- Subtitles smaller and on new line -->
    <xsl:template match="title[@type = 'sub']">
        <xsl:text xml:space="preserve"> </xsl:text>
        <br />
        <small>
            <xsl:apply-templates />
        </small>
    </xsl:template>

    <!-- Analysis reference as attribute in a div/span -->
    <xsl:template match="*[@ana]">
        <xsl:choose>
            <xsl:when test="tei:isInline(.)">
                <xsl:call-template name="makeSpan" />
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="makeBlock">
                    <xsl:with-param name="element" select="name()" />
                </xsl:call-template>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

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

    <xsl:template match="p|trailer">
        <xsl:call-template name="newline" />
        <xsl:apply-templates />
        <xsl:call-template name="newline" />
    </xsl:template>

    <xsl:template match="label">
        <xsl:apply-templates />
    </xsl:template>

    <!-- Poetry -->
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
        <xsl:text xml:space="preserve">    </xsl:text>
        <xsl:if test="@n">
            <xsl:number value="@n" format="1." />
            <xsl:text xml:space="preserve">  </xsl:text>
        </xsl:if>
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

        <xsl:text>{:</xsl:text>
        <xsl:if test="exists($id)">
            <xsl:text xml:space="preserve"> #</xsl:text>
            <xsl:value-of select="$id" />
        </xsl:if>
        <xsl:if test="exists($class)">
            <xsl:text xml:space="preserve"> .</xsl:text>
            <xsl:value-of select="$class" />
        </xsl:if>
        <xsl:if test="exists($title)">
            <xsl:text xml:space="preserve"> title="</xsl:text>
            <xsl:value-of disable-output-escaping="yes" select="$title" />
            <xsl:text xml:space="preserve">"</xsl:text>
        </xsl:if>
        <xsl:if test="exists($ana)">
            <xsl:text xml:space="preserve"> ana="</xsl:text>
            <xsl:value-of disable-output-escaping="yes" select="$ana" />
            <xsl:text xml:space="preserve">"</xsl:text>
        </xsl:if>
        <xsl:text xml:space="preserve"> }</xsl:text>
    </xsl:template>

    <!-- Links to external resources are rendered in markdown reference syntax -->
    <xsl:template match="*[@ref]">
        <xsl:value-of select="tei:mkLink(.,substring(@ref, 2),'reference')" />
        <xsl:call-template name="mkLinkAttrs">
            <xsl:with-param name="class" select="name()" />
        </xsl:call-template>
    </xsl:template>

    <!-- Pointers are rendered as regular markdown links with the text content of the target -->
    <xsl:template match="ptr">
        <xsl:variable name="target-text" select="id(substring(@target, 2))" />

        <xsl:value-of select="tei:mkLink($target-text,@target,'')" />
        <xsl:call-template name="mkLinkAttrs">
            <xsl:with-param name="class" select="'ref'" />
        </xsl:call-template>
    </xsl:template>

    <!-- In-line quotes call the link template if a corresp id is given -->
    <xsl:template match="q" priority="2">
        <xsl:text>«</xsl:text>
        <xsl:choose>
            <xsl:when test="@corresp">
                <xsl:call-template name="corresp" />
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates />
            </xsl:otherwise>
        </xsl:choose>
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
        <xsl:if test="title[@type='sub']">
            <xsl:call-template name="shortToc" />
        </xsl:if>
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

    <xsl:template name="shortToc">
        <xsl:text xml:space="preserve">{: data-toc-label="</xsl:text>
        <xsl:value-of select="title[not(@type='sub' or @xml:lang = $lang)]" separator=", " />
        <xsl:text xml:space="preserve">" }</xsl:text>
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
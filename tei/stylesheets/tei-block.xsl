<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
  version="3.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:tei="http://www.tei-c.org/ns/1.0"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:map="http://www.w3.org/2005/xpath-functions/map"
  xpath-default-namespace="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei xs map"
  default-mode="block">

  <!-- ===================================================
       TEI BLOCK‑LEVEL TEMPLATES
       =================================================== -->

  <!-- Wrap a block element in html tags with markdown flag -->
  <xsl:template name="wrap-block">
    <xsl:param name="title" as="item()*" select="()"/>
    <xsl:param name="element" as="xs:string?" select="'div'"/>
    <xsl:text>&#10;&lt;</xsl:text><xsl:value-of select="$element"/>
    <xsl:call-template name="html-attrs">
      <xsl:with-param name="attrs" select="map{
        'class': @type,
        'id': @xml:id,
        'title': $title
      }"/>
    </xsl:call-template>
    <xsl:text> markdown&gt;&#10;</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>&#10;&#10;&lt;/</xsl:text><xsl:value-of select="$element"/><xsl:text>&gt;&#10;</xsl:text>
  </xsl:template>

  <!-- Notes and lists: always render as blocks -->
  <xsl:template match="note|list" mode="#all">
    <xsl:call-template name="wrap-block"/>
  </xsl:template>

  <!-- Blockquote: always render as block -->
  <xsl:template match="quote" mode="#all">
    <xsl:call-template name="wrap-block">
      <xsl:with-param name="element" select="'blockquote'"/>
      <xsl:with-param name="title" select="parent::cit/bibl"/>
    </xsl:call-template>
  </xsl:template>

  <!-- Paragraphs and trailers -->
  <xsl:template match="p|trailer">
    <xsl:text>&#10;</xsl:text>
    <xsl:apply-templates mode="inline"/>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>

  <!-- Expandable content inside <details> -->
  <xsl:template match="*[@rendition='expandable']">
    <xsl:text>&lt;details markdown&gt;&#10;</xsl:text>
    <xsl:value-of select="tei:tag('summary','open')"/>
    <xsl:value-of select="tei:tag('summary','close')"/>
    <xsl:text>&#10;</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>&#10;&lt;/details&gt;&#10;</xsl:text>
  </xsl:template>

  <!-- Poem groups and lines -->
  <xsl:template match="lg">
    <xsl:if test="@n">
      <xsl:value-of select="@n"/><xsl:text>.  </xsl:text>
      <xsl:text>&#10;</xsl:text>
    </xsl:if>
    <xsl:apply-templates/>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>

  <xsl:template match="l">
    <xsl:choose>
      <xsl:when test="@n">
        <xsl:text>    </xsl:text>
        <xsl:number value="@n" format="1."/>
        <xsl:text>  </xsl:text>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>&#10;</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <xsl:apply-templates mode="inline"/>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>

  <!-- Titles and subtitles -->
  <xsl:template match="teiCorpus">
    <xsl:apply-templates select="TEI"/>
  </xsl:template>

  <xsl:template match="teiHeader">
    <xsl:apply-templates select="fileDesc/titleStmt"/>
  </xsl:template>

  <xsl:template match="titleStmt">
    <xsl:text>&#10;## </xsl:text>
    <xsl:apply-templates select="title"/>
  </xsl:template>

  <xsl:template match="title">
    <xsl:apply-templates mode="inline"/>
  </xsl:template>

  <xsl:template match="title[@type='short']">
    <xsl:text> </xsl:text>
        <xsl:call-template name="md-attrs">
          <xsl:with-param name="id" select="string(.)"/>
          <xsl:with-param name="attrs" select="map { 'data-toc-label': string(.) }"/>
        </xsl:call-template>
  </xsl:template>

  <xsl:template match="title[@type='sub']">
    <xsl:text>&#10;</xsl:text>
    <xsl:apply-templates mode="inline"/>
    <xsl:text>&#10;</xsl:text>
    <xsl:text>{: .subtitle }</xsl:text>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>

  <!-- Character list as reference targets -->
  <xsl:template match="listPerson">
    <xsl:apply-templates select="person"/>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>

  <xsl:template match="person">
    <xsl:call-template name="ref-target">
      <xsl:with-param name="id" select="@xml:id"/>
      <xsl:with-param name="url" select="@sameAs"/>
      <xsl:with-param name="title" select="persName"/>
    </xsl:call-template>
    <xsl:text>&#10;</xsl:text>
    <xsl:apply-templates select="persona"/>
  </xsl:template>

  <xsl:template match="persona">
    <xsl:call-template name="ref-target">
      <xsl:with-param name="id" select="@xml:id"/>
      <xsl:with-param name="url" select="parent::person/@sameAs"/>
      <xsl:with-param name="title" select="concat(persName,' (',parent::person/persName,').', tei:tag('br','open-close'), note)"/>
    </xsl:call-template>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>

  <!-- Headers -->
  <xsl:template match="head">
    <xsl:text>&#10;</xsl:text>
    <xsl:variable name="depth" select="tei:depth(..)"/>
    <xsl:choose>
      <xsl:when test="$depth=0">##</xsl:when>
      <xsl:when test="$depth=1">###</xsl:when>
      <xsl:when test="$depth=2">####</xsl:when>
      <xsl:when test="$depth=3">#####</xsl:when>
    </xsl:choose>
    <xsl:text> </xsl:text>
    <xsl:apply-templates/>
    <xsl:text>&#10;</xsl:text>
    <xsl:if test="parent::div/@resp">
      <xsl:variable name="resp" select="tei:defrag(parent::div/@resp)"/>
      <xsl:variable name="target" select="id($resp)"/>
      <xsl:variable name="title" select="
        if (name($target) = 'persona') 
        then concat($target/persName, ' (', $target/parent::person/persName, ')')
        else $target/persName"/>
      <xsl:call-template name="span">
        <xsl:with-param name="content" select="$title"/>
      </xsl:call-template>
      <xsl:call-template name="ref-link">
        <xsl:with-param name="target" select="$resp"/>
      </xsl:call-template>
      <xsl:text>&#10;&#10;</xsl:text>
    </xsl:if>
  </xsl:template>

  <!-- List items -->
  <xsl:template match="label">
    <xsl:apply-templates mode="inline"/>
  </xsl:template>

   <xsl:template match="item">
      <xsl:text>&#10;*  </xsl:text>
      <xsl:apply-templates mode="inline"/>
      <xsl:call-template name="item-attrs"/>
      <xsl:text>&#10;</xsl:text>
    </xsl:template>

    <xsl:template match="item[parent::list[@type='gloss']]">
      <xsl:text>&#10;:  </xsl:text>
      <xsl:apply-templates mode="inline"/>
      <xsl:call-template name="item-attrs"/>
      <xsl:text>&#10;&#10;</xsl:text>
    </xsl:template>

    <xsl:template match="item[parent::list[@type='syllogism']]">
      <xsl:text>&#10;*  </xsl:text>
      <xsl:variable name="target" select="if (ptr) then tei:defrag(ptr/@target) else ()"/>
      <xsl:variable name="label" select="if ($target) then $target else string(@xml:id)"/>
      <xsl:variable name="against" select="if ($target) then id($target)/@exclude => tei:defrag() else tei:defrag(@exclude)"/>
      <!-- Label -->
      <xsl:call-template name="span">
        <xsl:with-param name="content" select="concat($label, ' ')"/>
      </xsl:call-template>
      <xsl:call-template name="md-attrs">
        <xsl:with-param name="class" select="'label'"/>
      </xsl:call-template>
      <!-- Proposition -->
      <xsl:choose>
        <xsl:when test="ptr">
          <xsl:apply-templates mode="inline"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:call-template name="span"/>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:call-template name="md-attrs">
        <xsl:with-param name="class" select="'prop'"/>
      </xsl:call-template>
      <!-- Against -->
      <xsl:if test="$against">
        <xsl:call-template name="span">
          <xsl:with-param name="content" select="concat(' ✖ ', $against)"/>
        </xsl:call-template>
        <xsl:call-template name="md-attrs">
          <xsl:with-param name="class" select="'against'"/>
        </xsl:call-template>
      </xsl:if>
      <xsl:call-template name="item-attrs"/>
      <xsl:text>&#10;</xsl:text>
    </xsl:template>

  <!-- Attach xml:id, ana, exclude to list items -->
  <xsl:template name="item-attrs">
    <xsl:if test="@xml:id or @ana">
      <xsl:text>&#10;</xsl:text>
        <xsl:call-template name="md-attrs">
          <xsl:with-param name="id" select="@xml:id"/>
          <xsl:with-param name="attrs" select="map{ 'ana': @ana }"/>
        </xsl:call-template>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
  version="3.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:tei="http://www.tei-c.org/ns/1.0"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:map="http://www.w3.org/2005/xpath-functions/map"
  xpath-default-namespace="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei xs map"
  default-mode="inline">

  <!-- ===================================================
       TEI INLINE-LEVEL TEMPLATES
       =================================================== -->

  <!-- Collapse multiple spaces -->
  <xsl:template match="text()">
    <xsl:value-of select="replace(., '\s{2,}', '')"/>
  </xsl:template>

  <!-- Gap placeholder -->
  <xsl:template match="gap">
    <xsl:text>\[…\]</xsl:text>
  </xsl:template>

  <!-- Foreign (emphasis) -->
  <xsl:template match="emph|foreign">
    <xsl:call-template name="emph"/>
  </xsl:template>

  <!-- Mentioned (quotation marks) -->
  <xsl:template match="mentioned">
    <xsl:call-template name="double-quote"/>
  </xsl:template>

  <!-- Inline title -->
  <xsl:template match="title">
    <xsl:value-of select="tei:tag('em','open')" />
    <xsl:apply-templates/>
    <xsl:value-of select="tei:tag('em','close')" />
  </xsl:template>

  <!-- Inline note -->
  <xsl:template match="note[@place = 'inline']">
    <xsl:text>\[</xsl:text>
    <xsl:apply-templates/>
    <xsl:text>\]</xsl:text>
  </xsl:template>

  <!-- Analysis span -->
  <xsl:template match="seg[@ana]">
    <xsl:call-template name="span"/>
    <xsl:variable name="target" select="tei:defrag(@ana) => id()"/>
    <xsl:variable name="title" select="if ($target/self::tei:interp) then ($target/text() | $target/desc) else ''"/>
    <xsl:call-template name="md-attrs">
      <xsl:with-param name="id" select="tei:suffix-lang(@xml:id)"/>
      <xsl:with-param name="attrs" select="map{
        'ana': @ana,
        'title': $title
      }"/>
    </xsl:call-template>
  </xsl:template>

  <!-- Character reference -->
  <xsl:template match="*[@ref]">
    <xsl:call-template name="span"/>
    <xsl:call-template name="ref-link">
      <xsl:with-param name="target" select="tei:defrag(@ref)"/>
    </xsl:call-template>
  </xsl:template>

  <!-- Pointer (renders referenced content) -->
  <xsl:template match="ptr">
    <xsl:call-template name="span">
      <xsl:with-param name="content" select="tei:defrag(@target) => id()"/>
    </xsl:call-template>
    <xsl:call-template name="link">
      <xsl:with-param name="target" select="@target"/>
    </xsl:call-template>
  </xsl:template>

  <!-- Citations -->
  <xsl:template match="cit">
    <xsl:apply-templates select="quote|q"/>
  </xsl:template>

  <!-- Inline quote -->
  <xsl:template match="q" priority="2">
    <xsl:variable name="is-foreign" select="@type='foreign'"/>
    <xsl:text>«</xsl:text>
    <xsl:choose>
      <xsl:when test="@corresp">
        <xsl:call-template name="corresp"/>
      </xsl:when>
      <xsl:when test="parent::cit">
        <xsl:call-template name="span">
          <xsl:with-param name="emph" select="$is-foreign"/>
        </xsl:call-template>
        <xsl:call-template name="md-attrs">
          <xsl:with-param name="class" select="name()"/>
          <xsl:with-param name="attrs" select="map{ 'title': parent::cit/bibl }"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:when test="$is-foreign">
        <xsl:call-template name="emph"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates/>
      </xsl:otherwise>
    </xsl:choose>
    <xsl:text>»</xsl:text>
  </xsl:template>

  <!-- Inline cross-reference -->
  <xsl:template match="*[@corresp]" name="corresp">
    <xsl:variable name="is-foreign" select="@type='foreign'"/>
    <xsl:variable name="target" select="tei:defrag(@corresp) => id()"/>
    <xsl:variable name="title" select="if ($target/parent::l)
        then tei:poem-ref($target) => tei:norm-str()
        else tei:prose-ref($target) => tei:norm-str()"/>
    <xsl:call-template name="span">
      <xsl:with-param name="emph" select="$is-foreign"/>
    </xsl:call-template>
    <xsl:call-template name="link">
      <xsl:with-param name="target" select="tei:suffix-lang(@corresp)"/>
    </xsl:call-template>
    <xsl:call-template name="md-attrs">
      <xsl:with-param name="class" select="name()"/>
      <xsl:with-param name="attrs" select="map{ 'title': $title }"/>
    </xsl:call-template>
  </xsl:template>

</xsl:stylesheet>

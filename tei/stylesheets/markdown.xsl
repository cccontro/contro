<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
  version="3.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:tei="http://www.tei-c.org/ns/1.0"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:map="http://www.w3.org/2005/xpath-functions/map"
  xpath-default-namespace="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei xs map">

  <!-- ===================================================
       MARKDOWN TEMPLATES
       =================================================== -->

  <!-- Emphasis: *content* -->
  <xsl:template name="emph">
    <xsl:text>*</xsl:text>
    <xsl:apply-templates mode="inline"/>
    <xsl:text>*</xsl:text>
  </xsl:template>

  <!-- Double quotation marks: “content” -->
  <xsl:template name="double-quote">
    <xsl:text>“</xsl:text>
    <xsl:apply-templates mode="inline"/>
    <xsl:text>”</xsl:text>
  </xsl:template>

  <!-- Span: [content] or [*content*] -->
  <xsl:template name="span">
    <xsl:param name="content" select="()"/>
    <xsl:param name="emph" as="xs:boolean" select="false()"/>
    <xsl:text>[</xsl:text>
    <xsl:choose>
      <xsl:when test="$emph"><xsl:call-template name="emph"/></xsl:when>
      <xsl:when test="$content"><xsl:value-of select="$content"/></xsl:when>
      <xsl:otherwise><xsl:apply-templates mode="inline"/></xsl:otherwise>
    </xsl:choose>
    <xsl:text>]</xsl:text>
  </xsl:template>

  <!-- Inline link: (url) -->
  <xsl:template name="link">
    <xsl:param name="target" as="xs:string"/>
    <xsl:text>(</xsl:text><xsl:value-of select="$target"/><xsl:text>)</xsl:text>
  </xsl:template>

  <!-- Reference link: [id] -->
  <xsl:template name="ref-link">
    <xsl:param name="target" as="xs:string"/>
    <xsl:text>[</xsl:text><xsl:value-of select="$target"/><xsl:text>]</xsl:text>
  </xsl:template>

  <!-- Reference target: [id]: url "title" -->
  <xsl:template name="ref-target">
    <xsl:param name="id" as="xs:string"/>
    <xsl:param name="url" as="xs:string"/>
    <xsl:param name="title" as="item()*"/>
    <xsl:text>[</xsl:text><xsl:value-of select="$id"/><xsl:text>]: </xsl:text>
    <xsl:value-of select="$url"/>
    <xsl:if test="$title">
      <xsl:text> "</xsl:text>
      <xsl:call-template name="join-values">
        <xsl:with-param name="values" select="$title"/>
      </xsl:call-template>
      <xsl:text>"</xsl:text>
    </xsl:if>
  </xsl:template>

  <!-- Markdown attributes: {: #id .class key="value" } -->
  <xsl:template name="md-attrs">
    <xsl:param name="id" as="xs:string?"/>
    <xsl:param name="class" as="xs:string?"/>
    <xsl:param name="attrs" as="map(xs:string, item()*)?" select="()"/>
    <xsl:text>{:</xsl:text>
    <xsl:if test="$id"><xsl:text> #</xsl:text><xsl:value-of select="$id"/></xsl:if>
    <xsl:if test="$class"><xsl:text> .</xsl:text><xsl:value-of select="$class"/></xsl:if>
    <xsl:if test="exists($attrs)">
      <xsl:call-template name="html-attrs"><xsl:with-param name="attrs" select="$attrs"/></xsl:call-template>
    </xsl:if>
    <xsl:text> }</xsl:text>
  </xsl:template>

  <!-- HTML attributes: key="value" -->
  <xsl:template name="html-attrs">
    <xsl:param name="attrs" as="map(xs:string, item()*)"/>
    <xsl:for-each select="map:keys($attrs)">
      <xsl:variable name="k" select="."/>
      <xsl:variable name="v" select="$attrs($k)"/>
      <xsl:if test="normalize-space(string-join($v, '')) != ''">
        <xsl:text> </xsl:text><xsl:value-of select="$k"/>
        <xsl:text>="</xsl:text>
        <xsl:call-template name="join-values">
          <xsl:with-param name="values" select="$v"/>
        </xsl:call-template>
        <xsl:text>"</xsl:text>
      </xsl:if>
    </xsl:for-each>
  </xsl:template>

  <!-- Separates multiple attribute values with line breaks -->
  <xsl:template name="join-values">
    <xsl:param name="values" as="item()*"/>
    <xsl:choose>
      <xsl:when test="count($values) = 1">
        <xsl:apply-templates select="$values" mode="inline"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:for-each select="$values">
          <xsl:apply-templates select="." mode="inline"/>
          <xsl:if test="position() != last()">
            <xsl:value-of select="tei:tag('br', 'open-close')"/>
          </xsl:if>
        </xsl:for-each>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>

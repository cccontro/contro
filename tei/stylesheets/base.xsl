<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
  version="3.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:tei="http://www.tei-c.org/ns/1.0"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:map="http://www.w3.org/2005/xpath-functions/map"
  xpath-default-namespace="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei xs map">

  <!-- Output settings -->
  <xsl:output
    method="text"
    encoding="UTF-8"
    omit-xml-declaration="yes"/>

  <!-- Strip rules -->
  <xsl:strip-space elements="*"/>
  <xsl:preserve-space elements="p bibl"/>

  <!-- Parameters -->
  <xsl:param name="lang" as="xs:string" select="'en'"/>

  <!-- Discard non-matching translations, keep explicit foreign spans -->
  <xsl:template
    mode="#all"
    match="*[@xml:lang and not(@xml:lang = $lang)
             and not(self::tei:foreign)
             and not(@type='foreign')]"
    priority="10"/>

  <!-- Include modules -->
  <xsl:include href="functions.xsl"/>
  <xsl:include href="markdown.xsl"/>
  <xsl:include href="tei-block.xsl"/>
  <xsl:include href="tei-inline.xsl"/>

  <!-- Driver -->
  <xsl:template match="/">
    <xsl:apply-templates select="//standOff/listPerson" mode="block"/>
    <xsl:apply-templates select="//TEI" mode="block"/>
  </xsl:template>

</xsl:stylesheet>

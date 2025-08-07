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
       FUNCTIONS
       =================================================== -->

  <!-- Remove hashtag -->
  <xsl:function name="tei:defrag" as="xs:string">
    <xsl:param name="s" as="xs:string?"/>
    <xsl:sequence select="if ($s) then replace($s, '^#', '') else ''"/>
  </xsl:function>

  <!-- Wrap a raw tag name in escaped HTML brackets -->
  <xsl:function name="tei:tag" as="xs:string">
    <xsl:param name="element" as="xs:string"/>
    <xsl:param name="mode" as="xs:string"/>
    <xsl:choose>
      <xsl:when test="$mode = 'markdown'">
        <xsl:sequence select="concat('&lt;',$element,' markdown&gt;')"/>
      </xsl:when>
      <xsl:when test="$mode = 'open'">
        <xsl:sequence select="concat('&lt;',$element,'&gt;')"/>
      </xsl:when>
      <xsl:when test="$mode = 'close'">
        <xsl:sequence select="concat('&lt;/',$element,'&gt;')"/>
      </xsl:when>
      <xsl:when test="$mode = 'open-close'">
        <xsl:sequence select="concat('&lt;',$element,'/&gt;')"/>
      </xsl:when>
    </xsl:choose>
  </xsl:function>

  <!-- Compute heading depth based on ancestor divs with head -->
  <xsl:function name="tei:depth" as="xs:integer">
    <xsl:param name="div" as="element(tei:div)"/>
    <xsl:sequence select="count($div/ancestor::tei:div[tei:head])
                     + (if ($div/tei:head) then 1 else 0)"/>
  </xsl:function>

  <!-- Build prose reference: title, section, page/p.p. -->
  <xsl:function name="tei:prose-ref" as="xs:string">
    <xsl:param name="target" as="node()?"/>
    <xsl:variable name="ancestor" select="outermost($target/ancestor::tei:div)"/>
    <xsl:variable name="title" select="
      concat(
        tei:tag('em','open'),
        $ancestor//tei:title[not(@type='sub' or @xml:lang != $lang)],
        tei:tag('em','close')
      )"/>
    <xsl:variable name="section" select="concat(' ',$target/ancestor::tei:div[1]/@n)"/>
    <xsl:choose>
      <xsl:when test="$ancestor/@n">
        <xsl:sequence select="concat($title,$section,', p. ',$ancestor/@n)"/>
      </xsl:when>
      <xsl:when test="$ancestor/@from">
        <xsl:sequence select="concat($title,$section,', pp. ',$ancestor/@from,'–',$ancestor/@to)"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:sequence select="concat($title,$section)"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:function>

  <!-- Build poetic reference: first line, stanza and line numbers -->
  <xsl:function name="tei:poem-ref" as="xs:string">
    <xsl:param name="target" as="node()"/>
    <xsl:variable name="title" select="string-join(tei:poem-title($target))"/>
    <xsl:variable name="sections" select="string-join($target/ancestor::tei:lg/@n,', ')"/>
    <xsl:sequence select="concat($title,' ',$sections,', ',$target/parent::tei:l/@n)"/>
  </xsl:function>

  <!-- Extract poem title from first line, strip trailing punctuation -->
  <xsl:function name="tei:poem-title" as="xs:string">
    <xsl:param name="target" as="node()"/>
    <xsl:variable name="poem" select="outermost($target/ancestor::tei:lg)"/>
    <xsl:variable name="opening" select="head($poem//tei:l[1])"/>
    <xsl:sequence select="
      concat(
        tei:tag('em','open'),
        replace($opening,'[\p{P}\s]+$',''),
        tei:tag('em','close')
      )"/>
  </xsl:function>

  <!-- Append language suffix to an id, unless already present -->
  <xsl:function name="tei:suffix-lang" as="xs:string?">
    <xsl:param name="label" as="xs:string?"/>
    <xsl:sequence select="
      if (empty($label)) then ()
      else if (matches($label,'-[a-z]{2}$')) then $label
      else concat($label,'-',$lang)
    "/>
  </xsl:function>

  <!-- Normalize a string: drop if empty after trimming -->
  <xsl:function name="tei:norm-str" as="xs:string?">
    <xsl:param name="s" as="xs:string?"/>
    <xsl:variable name="norm" select="normalize-space($s)"/>
    <xsl:sequence select="if ($norm='' or $norm=concat(tei:tag('em','open'),tei:tag('em','close'))) then () else $s"/>
  </xsl:function>

</xsl:stylesheet>

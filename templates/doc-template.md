<!--- This file was automatically generated - do not edit -->

{#-
  Macro to render elements as details or divs
-#}
{% macro render_element(e) %}
  {% if e.is_detail %}
<details class="{{ e.owl_type|lower|replace(' ', '_') }}" name="element" markdown>
  <summary>
  <div class="overview">
  {% else %}
<div class="admonition {{ e.owl_type|lower|replace(' ', '_') }}" markdown>
  <div class="admonition-title overview">
  {% endif %}
    <div class="label">
      <h3 id="{{ e.href[1:] }}">{{ e.label }}</h3>
  {% if e.uri %}
      <a class="{{ e.owl_type|lower|replace(' ', '_') }}" href="{{ e.href }}">{{ e.uri }}</a>
  {% endif %}
    </div>
  {% for attr, label in e._base.items() %}
    {% if e[attr] %}
  <ul>
    <h4>{{ label }}</h4>
    {% for a in e[attr] %}
    <li>
      {{ a.html()|safe }}
    </li>
    {% endfor %}
  </ul>
    {% endif %}
  {% endfor %}
  </div>
  {% if e.desc %}
  <p class="description">{{ e.desc }}</p>
  {% endif %}
  {% if e.owl_type == 'Rule' %}
  <p>{{ e.rule }}</p>
  {% endif %}
  {% if e.is_detail %}
  </summary>
  <div class="extra">
  {% endif %}
  {% for attr, label in e._extra.items() %}
    {% if e[attr] %}
    <ul>
      <h4>{{ label }}</h4>
      {% for a in e[attr] %}
      <li>
        {{ a.html()|safe }}
      </li>
      {% endfor %}
    </ul>
    {% endif %}
  {% endfor %}
  {% if e.also_defined_as %}
    <ul>
      <h4>Also defined as</h4>
    {% for o in e.also_defined_as %}
      <li>
        <a class="{{ o.owl_type|lower|replace(' ', '_') }}" href="{{ o.href }}" title="{{ o.uri }}">{{ o.owl_type }}</a>
      </li>
    {% endfor %}
    </ul>
  {% endif %}
  </div>
  {% if e.is_detail %}
</details>
  {% endif %}
{% endmacro %}

{#
  Start of documentation
#}

{% if doc.title %}
<h1>{{ doc.title }}{% if doc.prefix %} <small>({{ doc.prefix }})</small>{% endif %}</h1>
{% endif %}

## Overview

{% for label, attr in doc.metadata %}
  {% if attr %}
**{{ label }}:** {{ attr }}

  {% endif %}
{% endfor %}
{% if doc.license %}
**License:** [![License: CC BY 4.0](https://img.shields.io/badge/-CC%20BY%204.0-lightgrey.svg?style=for-the-badge)]({{ doc.license }})
{% endif %}

**Available:**

[![Format: TTL](https://img.shields.io/badge/Format-TTL-green.svg?style=for-the-badge)]({{ doc.uri }}.ttl)
[![Format: XML/RDF](https://img.shields.io/badge/Format-XML/RDF-red.svg?style=for-the-badge)]({{ doc.uri }}.owl)
[![Format: JSON-LD](https://img.shields.io/badge/Format-JSON--LD-blue.svg?style=for-the-badge)]({{ doc.uri }}.jsonld)

{% if doc.description %}
### Description
{{ doc.description }}
{% endif %}

### Namespaces

| Prefix | URI |
|--------|-----------|
{% for prefix, uri in doc.namespaces.items() %}
  {% if prefix %}
| {{ prefix }} | <{{ uri }}> |
  {% else %}
| base | <{{ uri }}> |
  {% endif %}
{% endfor %}

{% for (type_label, type) in doc.elements %}
  {% if type %}
## {{ type_label }}
  {% endif %}

  {% for e in type %}
{{ render_element(e) }}
  {% endfor %}
{% endfor %}
import markdown
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
import re

class SpanProcessor(InlineProcessor):
    """
    Allows inline content to be wrapped in a <span> element with custom attributes using the syntax:

        [content]{: #id .class key='value' }

    Supports nesting of both inline and reference-style Markdown links:

        [Some [inline](#ref){: title="Tooltip" } link]{: #span1 }
        [Some [reference][ref] link]{: #span2 }

    Regex logic:
    1. (?<!\\]) – Negative lookbehind:
       Ensures the opening [ is not immediately preceded by ].
       Prevents matching the second [ in a reference link.

    2. (?![^\\[]+\\][\\[\\(]) – Negative lookahead:
       Ensures any contained ]( or ][ are preceded by an additional opening [.
       Prevents matching the first [ of a link.

    3. (.+?) – Lazy capture of the content inside [ ... ]:
       Captures arbitrary inline content including any Markdown link.

    4. \\{\\s*([^\\}]+)\\s*\\} – Attribute block:
       Captures id, class, and key="value" pairs inside {...}.
    """
    RE = r'(?<!\])\[(?![^\[]+\][\[\(])(.+?)\]\{\s*([^\}]+)\s*\}'

    def handleMatch(self, m, data):
        text, attr_str = m.group(1), m.group(2)
        el = etree.Element('span')
        el.text = text

        class_list = []
        for token in re.finditer(r'(#[\w-]+)|(\.[\w-]+)|(\w+)="(.*?)"', attr_str):
            if token.group(1):  # #id
                el.set('id', token.group(1)[1:])
            elif token.group(2):  # .class
                class_list.append(token.group(2)[1:])
            elif token.group(3):  # key='value'
                el.set(token.group(3), token.group(4))

        if class_list:
            el.set('class', ' '.join(class_list))

        return el, m.start(0), m.end(0)

class SpanExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(SpanProcessor(SpanProcessor.RE, md), 'customspan', 175)

def makeExtension(**kwargs):
    return SpanExtension(**kwargs)
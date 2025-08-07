import os
import re
import argparse
from saxonche import PySaxonProcessor
from lxml import html
import write_if_changed, make_value


def main():
  parser = argparse.ArgumentParser(description='Convert a TEI ODD file to HTML')
  parser.add_argument('odd_path', help='path to the input .odd file')
  parser.add_argument('tei_dir', help='path to the TEI Stylesheets directory')

  args = parser.parse_args()

  name = os.path.basename(args.odd_path).split('.')[0]
  out_path = os.path.join(os.path.dirname(args.odd_path), f'{name}.html')

  # Stylesheets
  xslt_path1 = os.path.join(args.tei_dir, 'odds', 'odd2odd.xsl')
  xslt_path2 = os.path.join(args.tei_dir, 'odds', 'odd2lite.xsl')
  xslt_path3 = os.path.join(args.tei_dir, 'html', 'html.xsl')

  # Parameters
  params = {
    'lang': 'en',
    'defaultSource': os.path.join(os.getcwd(), args.tei_dir, 'source', 'p5subset.xml'), # TEI ODD for merging
    'cssFile': '', # no embedded CSS
    'cssPrintFile': '',
    'autoToc': 'false', # no table of contents
    'numberHeadings': 'false', # no numbered headers
    'divOffset': 2 # text headers start from <h2>
  }

  with PySaxonProcessor(license=False) as proc:
    xslt_proc = proc.new_xslt30_processor()

    # Parameters
    for k, v in params.items():
      xslt_proc.set_parameter(k, make_value(v, proc))

    # Step 1: ODD integration
    result1 = xslt_proc.transform_to_string(
      source_file=args.odd_path,
      stylesheet_file=xslt_path1
    )

    # Step 2: ODD to TEI Lite
    trans2 = xslt_proc.compile_stylesheet(stylesheet_file=xslt_path2)
    trans2.set_global_context_item(file_name=xslt_path2)
    doc2 = proc.parse_xml(xml_text=result1)
    result2 = trans2.apply_templates_returning_string(xdm_value=doc2)

    # Step 3: TEI to HTML
    trans3 = xslt_proc.compile_stylesheet(stylesheet_file=xslt_path3)
    trans3.set_global_context_item(file_name=xslt_path3)
    doc3 = proc.parse_xml(xml_text=result2)
    result = trans3.apply_templates_returning_string(xdm_value=doc3)

  # Post-processing
  tree = html.fromstring(result)

  # 1. Convert all <div class="pre"> to <pre> elements
  for div in tree.xpath('//div[contains(@class, "pre")]'):
    div.tag = 'pre'
    classes = div.get('class', '').split()
    filtered = [c for c in classes if c != 'pre']
    if filtered:
      div.set('class', ' '.join(filtered))
    else:
      div.attrib.pop('class', None)

  # 2. Replace <> with ＜＞ in titles for tooltip compatibility
  for a in tree.xpath('//a[@title]'):
    a.attrib['title'] = a.attrib['title'].replace('<', '＜').replace('>', '＞')

  # 3. Add Markdown boolean attribute to containers of headers
  for heading in tree.xpath('//*[starts-with(name(), "h") and span[@class="head"]]'):
    parent = heading.getparent()
    while parent is not None:
      parent.set('markdown')
      parent = parent.getparent()

  # 4. Select only the <body> content and add newline characters around <div> elements
  body = tree.find('body')
  content = '\n'.join([html.tostring(el, encoding='unicode', method='html') for el in body])
  pattern = re.compile(r'(?=<div)|(?<=</div>)')
  content = pattern.sub(r'\n', content)

  write_if_changed(content, out_path)


if __name__ == '__main__':
  main()

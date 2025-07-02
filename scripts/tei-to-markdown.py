import os
import argparse

from saxonche import PySaxonProcessor

import write_if_changed

def main():
  parser = argparse.ArgumentParser(description='Convert a XML-TEI file to HTML-in-Markdown.')
  parser.add_argument('xslt_path', help='Path to the input .xsl file.')
  parser.add_argument('xml_path', help='Path to the input .xml file.')

  args = parser.parse_args()

  for lang in ['en', 'it']:
    name = os.path.basename(args.xml_path).split('.')[0]
    md_path = os.path.join(os.path.dirname(args.xml_path), f'{name}-{lang}.md')

    with PySaxonProcessor(license=False) as proc:
      xslt_proc = proc.new_xslt30_processor()
      xslt_proc.set_parameter('lang', proc.make_string_value(lang))
      result = xslt_proc.transform_to_string(
        source_file=args.xml_path,
        stylesheet_file=args.xslt_path
      )
      write_if_changed(result, md_path)

if __name__ == '__main__':
  main()
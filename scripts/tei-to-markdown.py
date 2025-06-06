import os
import argparse
from saxonche import PySaxonProcessor

def write_if_changed(new, path):
  if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
      old = f.read()
    if old == new:
      return False
  with open(path, 'w', encoding='utf-8') as f:
    f.write(new)
  return True

def main():
  parser = argparse.ArgumentParser(description='Convert a XML-TEI file to HTML-in-Markdown.')
  parser.add_argument('xml_path', help='Path to the input .xml file.')
  parser.add_argument('xslt_path', help='Path to the input .xsl file.')

  args = parser.parse_args()

  for excluded_lang, output_lang in [('it', 'en'), ('en', 'it')]:
    filename = os.path.basename(args.xml_path).split('.')[0]
    output_name = f'{filename}.md' if output_lang == 'en' else f'{filename}-{output_lang}.md'
    output_path = os.path.join(os.path.dirname(args.xml_path), output_name)

    with PySaxonProcessor(license=False) as proc:
      xslt_proc = proc.new_xslt30_processor()
      xslt_proc.set_parameter('lang', proc.make_string_value(excluded_lang))
      result = xslt_proc.transform_to_string(
        source_file=args.xml_path,
        stylesheet_file=args.xslt_path
      )
      write_if_changed(result, output_path)

if __name__ == '__main__':
  main()
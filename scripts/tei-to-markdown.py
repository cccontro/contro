import os
import argparse
from saxonche import PySaxonProcessor
import write_if_changed

def main():
    parser = argparse.ArgumentParser(description='Convert an XML/TEI file to Markdown')
    parser.add_argument('xml_path', help='path to the input .xml file')
    parser.add_argument('xslt_path', help='path to the input .xsl file')
    parser.add_argument(
        '--lang',
        nargs='*',
        help='languages to filter the document by, leave empty for no filter'
    )

    args = parser.parse_args()

    langs = args.lang if args.lang else [None]

    for lang in langs:
        name = os.path.basename(args.xml_path).split('.')[0]
        suffix = f'-{lang}' if lang else ''
        md_path = os.path.join(os.path.dirname(args.xml_path), f'{name}{suffix}.md')

        with PySaxonProcessor(license=False) as proc:
            xslt_proc = proc.new_xslt30_processor()
            if lang:
                xslt_proc.set_parameter('lang', proc.make_string_value(lang))
            result = xslt_proc.transform_to_string(
                source_file=args.xml_path,
                stylesheet_file=args.xslt_path
            )
            write_if_changed(result, md_path)

if __name__ == '__main__':
    main()
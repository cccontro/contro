import os
import argparse
import subprocess
from saxonche import PySaxonProcessor

def main():
  parser = argparse.ArgumentParser(description='Convert an ODD TEI file to RELAX NG Compact')
  parser.add_argument('odd_path', help='path to the input .odd file')
  parser.add_argument('tei_dir', help='path to the TEI Stylesheets directory')
  parser.add_argument('trang_path', help='path to the Trang jar')

  args = parser.parse_args()

  name = os.path.basename(args.odd_path).split('.')[0]
  odd_dir = os.path.dirname(args.odd_path)
  comp_path = os.path.join(odd_dir, f'{name}-compiled.odd')
  rng_path = os.path.join(odd_dir, f'{name}.rng')
  rnc_path = os.path.join(odd_dir, f'{name}.rnc')

  # Stylesheets
  xslt_path1 = os.path.join(args.tei_dir, 'odds', 'odd2odd.xsl')
  xslt_path2 = os.path.join(args.tei_dir, 'odds', 'odd2relax.xsl')

  # TEI ODD for merging
  tei_odd_path = os.path.join(os.getcwd(), args.tei_dir, 'source', 'p5subset.xml')

  with PySaxonProcessor(license=False) as proc:
    xslt_proc = proc.new_xslt30_processor()

    # Parameters
    xslt_proc.set_parameter('defaultSource', proc.make_string_value(tei_odd_path))

    # Step 1: ODD integration
    xslt_proc.transform_to_file(
      source_file=args.odd_path,
      stylesheet_file=xslt_path1,
      output_file=comp_path
    )

    # Step 2: ODD to RNG
    xslt_proc.transform_to_file(
      source_file=comp_path,
      stylesheet_file=xslt_path2,
      output_file=rng_path
    )

  # Step 3: RNG to RNC
  subprocess.run(
    ['java', '-jar', args.trang_path, '-O', 'rnc', rng_path, rnc_path],
    check=True
  )

  # Clean up
  os.remove(comp_path)
  os.remove(rng_path)


if __name__ == '__main__':
    main()

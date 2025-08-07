import os
import subprocess
import logging
import time

import mkdocs.plugins

log = logging.getLogger('mkdocs')

def on_startup(command, dirty):
  start = time.monotonic()
  log.info('Converting ontologies and TEI resources...')

  # Configuration
  tbox_names = ['arg', 'persp', 'contro', 'data']
  abox_names = ['example', 'data']
  langs = ['en', 'it']
  text_lang = 'it'
  ann_lang = 'en'

  # Paths
  ## Ontology
  docs_dir = os.path.join(os.getcwd(), 'docs')
  elements_dir = os.path.join(docs_dir, 'elements')

  def get_ont_path(name):
    return os.path.join(docs_dir, 'ont', f'{name}.ttl')

  ontexport_jar = os.path.join('tools', 'ontexport', 'app', 'build', 'libs', 'ontexport.jar')
  doc_template = os.path.join('templates', 'doc-template.md')

  ## TEI text
  tei_path = os.path.join('tei', 'Apologia-Ragione-TEI.xml')
  tei_to_md_xslt = os.path.join('tei', 'stylesheets', 'tei-to-markdown', 'tei-to-markdown-custom.xsl')

  ## TEI schema
  odd_path = os.path.join('tei', 'tei_arg.odd')
  rnc_path = os.path.join('tei', 'tei_arg.rnc')
  tei_stylesheets_dir = os.path.join('tei', 'stylesheets', 'official')
  trang_jar = os.path.join('tools', 'trang', 'trang.jar')
  jing_jar = os.path.join('tools', 'jing', 'jing.jar')

  ## Scripts
  ont_doc_script = os.path.join('scripts', 'run-doc-template.py')
  tei_to_md_script = os.path.join('scripts', 'tei-to-markdown.py')
  tei_to_ttl_script = os.path.join('scripts', 'tei-to-turtle.py')
  odd_to_html_script = os.path.join('scripts', 'odd-to-html.py')
  odd_to_rnc_script = os.path.join('scripts', 'odd-to-rnc.py')

  # Step 1: Preprocess TEI schema
  subprocess.run(['python', odd_to_html_script, odd_path, tei_stylesheets_dir], check=True)
  subprocess.run(['python', odd_to_rnc_script, odd_path, tei_stylesheets_dir, trang_jar], check=True)

  # Step 2: Validate TEI against schema
  validation = subprocess.run(
    ['java', '-jar', 'tools/jing/jing.jar', '-c', 'tei/tei_arg.rnc', 'tei/Apologia-Ragione-TEI.xml'],
    stdout=subprocess.PIPE,
    text=True
  )
  if validation.returncode:
    log.error(f'TEI validation failed:{validation.stdout.split(':', 4)[4]}')
  else:
    log.info('TEI validation successful')

  # Step 3: Convert TEI to Markdown
  subprocess.run(['python', tei_to_md_script, tei_path, tei_to_md_xslt, '--lang', *langs], check=True)

  # Step 4: Extract argument instances to TTL
  subprocess.run(['python', tei_to_ttl_script, tei_path, get_ont_path('data'), '--text', text_lang, '--ann', ann_lang], check=True)

  # Step 5: Serialize RDF and infer ABoxes
  subprocess.run(
    ['java', '-jar', ontexport_jar, os.path.join(docs_dir, 'ont'), '--abox'] +
    [f'{abox}.ttl' for abox in abox_names],
    check=True
  )

  # Step 6: Generate documentation for each TBox
  for tbox in tbox_names:
    subprocess.run(
      ['python', ont_doc_script, get_ont_path(tbox), elements_dir, doc_template],
      check=True
    )

  # Summary
  duration = time.monotonic() - start
  if abox_names:
    log.info(f'Converted {len(tbox_names)} ontologies and reasoned over {len(abox_names)} in {duration:.2f} seconds')
  else:
    log.info(f'Converted {len(tbox_names)} ontologies in {duration:.2f} seconds')

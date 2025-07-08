import os
import subprocess
import logging
import time

import mkdocs.plugins

log = logging.getLogger('mkdocs')

def on_startup(command, dirty):
  start = time.monotonic()
  log.info('Converting ontologies...')

  tboxes = ['arg', 'persp', 'contro', 'data']
  aboxes = ['example', 'data']
  langs = ['en', 'it']
  text_lang = 'it'
  ann_lang = 'en'

  docs_dir = os.path.join(os.getcwd(), 'docs')
  tei_path = os.path.join('tei', 'Apologia-Ragione-TEI.xml')
  xslt_path = os.path.join('tei', 'stylesheets', 'tei-to-markdown-custom.xsl')
  jar_path = os.path.join('ontexport', 'app', 'build', 'libs', 'ontexport.jar')
  template = os.path.join('templates', 'doc-template.md')

  def ont(name):
    return os.path.join(docs_dir, 'ont', f'{name}.ttl')

  # 1. Convert the XML/TEI text to Markdown
  subprocess.run(['python', os.path.join('scripts', 'tei-to-markdown.py'), tei_path, xslt_path, '--lang', *langs], check=True)

  # 2. Populate data.ttl with argument instances extracted from the texts
  subprocess.run(['python', os.path.join('scripts', 'tei-to-turtle.py'), tei_path, ont('data'), '--text', text_lang, '--ann', ann_lang], check=True)

  # 3. Serialize XML/RDF and JSONLD from TTL files and export inferred axioms for ABoxes
  subprocess.run(
    ['java', '-jar', jar_path, os.path.join(docs_dir, 'ont'), '--abox'] + \
    [f'{abox}.ttl' for abox in aboxes],
    check=True
  )

  # 4. Generate ontology documentation
  for tbox in tboxes:
    subprocess.run(['python', os.path.join('scripts', 'run-doc-template.py'), ont(tbox), os.path.join(docs_dir, 'elements'), template], check=True)

  if aboxes:
    log.info(f'Converted {len(tboxes)} and reasoned on {len(aboxes)} ontologies in {time.monotonic() - start:.2f} seconds')
  else:
    log.info(f'Converted {len(tboxes)} ontologies in {time.monotonic() - start:.2f} seconds')
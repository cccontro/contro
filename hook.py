import os
import subprocess

def on_pre_build(config):
  docs_dir = config['docs_dir']
  xml_path = os.path.join(docs_dir, 'tei', 'Apologia-TEI.xml')
  xslt_path = os.path.join(docs_dir, 'tei', 'stylesheets', 'tei-to-markdown-custom.xsl')
  ttl_path = os.path.join(docs_dir, 'ont', 'data.ttl')

  subprocess.run(['python', os.path.join(docs_dir, 'tei', 'transformation.py'), xml_path, xslt_path])
  subprocess.run(['python', os.path.join(docs_dir, 'ont', 'conversion.py'), xml_path, ttl_path])
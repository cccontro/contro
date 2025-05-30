import os
import subprocess

def on_pre_build(config):
  docs_dir = config['docs_dir']
  xml_path = os.path.join('tei', 'Apologia-TEI.xml')
  xslt_path = os.path.join('tei', 'stylesheets', 'tei-to-markdown-custom.xsl')
  templ_path = os.path.join('templates', 'doc-template.md')

  def ont(name):
    return os.path.join(docs_dir, 'ont', f'{name}.ttl')

  subprocess.run(['python', os.path.join('scripts', 'tei-to-markdown.py'), xml_path, xslt_path], check=True)
  subprocess.run(['python', os.path.join('scripts', 'tei-to-turtle.py'), xml_path, ont('data')], check=True)

  for ont_name in ['arg', 'persp', 'contro', 'data']:
    subprocess.run(['python', os.path.join('scripts', 'run-doc-template.py'), ont(ont_name), os.path.join(docs_dir, 'elements'), templ_path], check=True)
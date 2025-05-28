import os
import argparse
from jinja2 import Environment, FileSystemLoader
import ontdoc as od

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
    parser = argparse.ArgumentParser(description='Render ontology documentation with template.')
    parser.add_argument('ttl_path', help='Path to the input .ttl file.')
    parser.add_argument('out_dir', help='Path to the output folder.')
    parser.add_argument('templ_path', help='Path to the Jinja template file.')

    args = parser.parse_args()

    # Set up Jinja environment
    templ_dir, templ_name = os.path.split(args.templ_path)

    env = Environment(
        loader=FileSystemLoader(templ_dir),
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=False  # Allow raw HTML/Markdown
    )

    template = env.get_template(templ_name)
    doc = od.OntDoc(args.ttl_path)
    output = template.render(doc=doc)

    ont_name = os.path.basename(args.ttl_path)
    out_path = os.path.join(args.out_dir, f'{os.path.splitext(ont_name)[0]}.md')

    write_if_changed(output, out_path)


if __name__ == '__main__':
  main()
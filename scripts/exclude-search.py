import mkdocs.plugins
from lxml import html

def on_page_content(html_content, page, config, files):
  if page.title != 'Examples':
    return html_content

  tree = html.fromstring(html_content)

  # Find all the tabbed-blocks
  for parent in tree.xpath('.//div[@class="tabbed-content"]'):
    tabs = parent.xpath('./div[@class="tabbed-block"]')[1:] # keep the first tab in search
    for tab in tabs:
      headers = tab.xpath('.//h1|.//h2|.//h3|.//h4|.//h5|.//h6')
      for header in headers:
        header.attrib['data-search-exclude'] = ''

  return html.tostring(tree, encoding='unicode')
source_suffix = {
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'
project = 'Manuel'
copyright = 'Benji York'
version = '1'
release = '1'
today_fmt = '%Y-%m-%d'
pygments_style = 'sphinx'

html_last_updated_fmt = '%Y-%m-%d'
html_title = 'Manuel Documentation'

todo_include_todos = False
exclude_dirnames = ['manuel.egg-info']
unused_docs = ['manuel/capture']

# html_theme = 'nature'
html_theme = "sphinx_book_theme"

extensions = [
    "myst_parser",
]
myst_enable_extensions = [
    "deflist",
]
exclude_patterns = ['capture.txt']

import os

data = {
    'site_name': 'My Docs',
    'theme': 'readthedocs',
    'plugins': ['search', ],
    'pages': ['index: index.md']
}
cur_path = os.getcwd()
# ul = os.listdir(os.path.join(cur_path, 'docs'))
ul = os.listdir('docs')

data['pages'] = ul
with open('mkdocs.yml', 'w+', encoding='utf-8') as f:
    for k, vs in data.items():

        if isinstance(vs, list):
            f.write('{}:\n'.format(k))
            for v in vs:
                f.write('    - {}\n'.format(v))

        else:
            f.write('{}: {}\n'.format(k, vs))

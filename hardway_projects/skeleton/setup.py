try:
   from setuptools import setup
except ImportError:
   from distutils.core import setup
config = {
'description': 'My Project',
'author': 'Jsw',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': '1736219667@qq.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['hardwaygames'],
'scripts': [],
'name': 'hardway_project'
}
setup(**config)
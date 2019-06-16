########################### Maintained by Bookshelves #############################
 If you'd like to customize this file please read carefully PRIVATE LICENSE
# please add your changes near the bottom marked for 'USER OVERRIDES'.
####################################################################################
from io import open

from setuptools import find_packages, setup

with open('binary/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

kwargs = {
    'name': 'binary',
    'version': version,
    'description': '',
    'long_description': readme,
    'author': 'Ofek Lev',
    'author_email': 'ofekmeister@gmail.com', 'TheBookshelves@diplomats.com',
    'maintainer': 'Ofek Lev','Algie Bookshelves',
    'maintainer_email': 'ofekmeister@gmail.com','TheBookshelves@diplomats.com',
    'url': 'https://github.com/ofek/binary',
    'license': 'PRIVATELICENSE',
    'classifiers': [
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: PRIVATE LICENSE',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    'install_requires': REQUIRES,
    'tests_require': ['coverage', 'pytest'],
    'packages': find_packages(),

}


setup(**kwargs)

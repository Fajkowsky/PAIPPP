# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'Django==1.5.4',

]

dependency_links = [
    'git+https://github.com/django-nonrel/django@nonrel-1.3',
    'git+https://github.com/django-nonrel/djangotoolbox@toolbox-1.3',
    'git+https://github.com/django-nonrel/mongodb-engine@mongodb-engine-1.3',
]

if __name__ == '__main__':
    setup(name='dyszka',
          version='0.1',
          author=[],
          author_email=[],
          packages=find_packages(),
          install_requires=install_requires,
          dependency_links=dependency_links,
          )

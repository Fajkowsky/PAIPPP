# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'Django==1.5.4',
]

dependency_links = [
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
import codecs
from setuptools import setup, find_packages

with codecs.open('README.md', 'r', 'utf-8') as file:
    long_description = file.read()
    
setup(
    name = 'platron',
    version = '1.0.0',
    packages = find_packages(exclude=['tests']),
    install_requires = ['requests>=2.6', 'six'],
    author = 'Platron',
    author_email = 'it@platron.ru',
    description = 'A client library for the Platron API',
    long_description = long_description,
    keywords = 'platron payment api',
    url = 'https://github.com/Platron/python-sdk',
)
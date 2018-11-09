import codecs
from setuptools import setup, find_packages

setup(
    name='platron',
    version='2.2.0',
    packages=['platron', 'platron.request.request_builders', 'platron.request.data_objects', 'platron.request.clients',
              'platron.callback'],
    install_requires=['requests>=2.6', 'six', 'dicttoxml'],
    author='Platron',
    author_email='it@platron.ru',
    description='A client library for the Platron API',
    keywords='platron payment api',
    url='https://github.com/Platron/python-sdk',
)

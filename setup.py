from distutils.core import setup

setup(
    name='logmatic-python',
    version='0.1.6a0',
    author='Logmatic.io support team',
    author_email='support@logmatic.io',
    packages = ['logmatic'],
    scripts=[],
    url='https://github.com/jimabramson/logmatic-python',
    download_url =
    'https://github.com/jimabramson/logmatic-python/tarball/0.1.6a0',
    license='MIT',
    long_description=open('README.rst').read(),
    description='Python plugin to send logs to Logmatic.io',
    install_requires = ['python-json-logger'],
    keywords = ['logmatic']
)

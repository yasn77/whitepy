from setuptools import setup, find_packages

try:
    import pypandoc
    long_description=pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = "Whitespace interpreter written in Python 3"

setup(
    name='whitepy',
    version='0.0.1',
    author='Yasser Nabi',
    author_email='yassersaleemi@gmail.com',
    packages=['whitepy'],
    scripts=['whitepycli'],
    package_data={'README.md': ['README.md']},
    url='http://pypi.python.org/pypi/whitepy/',
    license='LICENSE.txt',
    description='Whitespace interpreter written in Python 3',
    long_description=long_description,
    install_requires=[
        "click == 6.7",
        "readchar == 0.7",
    ],
)

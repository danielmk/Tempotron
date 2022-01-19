from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tempotron',
    version='0.0.1',
    description='Fork of a tempotron implementation.',
    long_description=readme,
    author='Daniel Müller-Komorowska',
    author_email='danielmuellermsc@gmail.com',
    url='https://github.com/danielmk/Tempotron',
    license=license,
    packages=['tempotron'],
    install_requires=[
          'numpy',
          'numba',
          'matplotlib'
      ])

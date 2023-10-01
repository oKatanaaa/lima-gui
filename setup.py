from distutils.core import setup
from setuptools import find_packages


with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='lima-gui',
    version='0.4.1',
    description='A simple GUI utility for gathering LIMA-like chat data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Kilbas Igor',
    author_email='igor.kibas.ai@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    install_requires=requirements
)
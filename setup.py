from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='persian_syllable',
    version='1.0.0',
    description='This library can count the syllables of persian text or words by converting the persian text to finglish format',
    long_description=readme,
    author='Nbic',
    long_description_content_type="text/markdown",
    url="https://github.com/salsina/Persian-syllable-counter/",
    packages=find_packages(),
)
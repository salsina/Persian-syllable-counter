from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='persian_syllable_counter',
    version='1.0.0',
    description='This library can count the syllables of persian text or words by converting the persian text to finglish format',
    long_description=readme,
    author='Nbic',
    long_description_content_type="text/markdown",
    packages=find_packages(include=["persian_syllable_counter*"]),
    url="https://github.com/salsina/Persian-syllable-counter",
    install_requires=[],

    keywords=['python', 'first package'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ]
)
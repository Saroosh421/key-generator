"""Module for setting up the key_generator package."""
from setuptools import setup
def readme():
    """Read the contents of the README file and return as a string."""
    with open('README.md', encoding='utf-8') as readme_file:
        README = readme_file.read()
    return README
setup(
    name="key_generator",
    version="1.0.3",
    description="A Simple python package to generate customizable keys.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sahith02/key-generator",
    author="Sahith Kurapati",
    author_email="sahith02@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["key_generator"],
    include_package_data=True,
    install_requires=[],
)

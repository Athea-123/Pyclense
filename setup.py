from setuptools import setup, find_packages

setup(
  name="Pyclense",
  version="0.1.0",
  author="Group Geng2x", 
  description="A simple Python library for data cleaning and preprocessing.",
  long_description=open("README.md").read() if open("README.md").read() else"",
  long_description_content_types="text/markdown",
  url="https://github.com/Athea-123/Pyclense",
  packages=find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  install_requires=[
    "pandas",
    "numpy"
  ],
  

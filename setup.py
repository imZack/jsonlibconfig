from setuptools import setup
import os


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), "r") as f:
        return f.read()

setup(
    name="jsonlibconfig",
    version="0.0.1",
    description=":sparkles: Pure python implementation library" +
    " provides JSON <- convert -> Libconfig",
    long_description=read("README.md"),
    url="https://github.com/imZack/json-libconfig",
    author="YuLun Shih",
    author_email="shih@yulun.me",
    license="MIT",
    packages=["jsonlibconfig"],
    install_requires=["ply"],
    scripts=["bin/jsonlibconfig"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)

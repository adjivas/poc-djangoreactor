import re
from os.path import abspath, dirname, join

from setuptools import find_packages, setup

VERSION_RE = re.compile(r"__version__\s*=\s*\"(.*?)\"")
PROJECT_NAME = "navi2"

current_path = abspath(dirname(__file__))

with open(join(current_path, "config/__init__.py")) as file:
    result = VERSION_RE.search(file.read())
    if result is None:
        raise Exception("could not find package version")
    __version__ = result.group(1)

setup(
    name=PROJECT_NAME,
    description="This is a template for a project using Python Django.",
    author="Full Name",
    author_email="email@42network.org",
    version=__version__,
    packages=find_packages(),
    scripts=["manage.py"],
    zip_safe=True,
)

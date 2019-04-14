#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Our version ALWAYS matches the version of Django we support
# If Django has a new release, we branch, tag, then update this setting after the tag.
version = "0.1.0"

if sys.argv[-1] == "tag":
    os.system('git tag -a %s -m "version %s"' % (version, version))
    os.system("git push --tags")
    sys.exit()

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-django-webpack",
    version=version,
    description="A Cookiecutter template for creating production-ready Django & Webpack projects quickly.",
    long_description=long_description,
    author="Kiran Capoor",
    author_email="kiran.capoor94@gmail.com",
    url="https://github.com/kiran-capoor94/cookiecutter-django-webpack",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 2.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py"
    ),
)

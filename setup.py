"""This setup script packages pyblish_nuke"""

import os
import sys
from setuptools import setup, find_packages

version = []

with open("pyblish_nuke/version.py") as f:
    for line in f:
        if not line.startswith("VERSION_"):
            continue
        _, v = line.rstrip().split(" = ")
        version += [v]

version = ".".join(version)


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]


setup(
    name="pyblish-nuke",
    version=version,
    packages=find_packages(),
    url="https://github.com/pyblish/pyblish-nuke",
    license="LGPL",
    author="Abstract Factory and Contributors",
    author_email="marcus@abstractfactory.io",
    description="Maya Pyblish package",
    zip_safe=False,
    classifiers=classifiers,
    package_data={"pyblish_nuke": ["plugins/*.py", "nuke_path/*.py", "*.png"]]},
    install_requires=["pyblish-base>=1.4"],
)

"""This setup script packages pyblish_nuke"""

import os
import sys
from setuptools import setup, find_packages


## https://github.com/epfl-scitas/spack/blob/af6a3556c4c861148b8e1adc2637685932f4b08a/lib/spack/llnl/util/lang.py#L595-L622
def load_module_from_file(module_name, module_path):
    """Loads a python module from the path of the corresponding file.
    Args:
        module_name (str): namespace where the python module will be loaded,
            e.g. ``foo.bar``
        module_path (str): path of the python file containing the module
    Returns:
        A valid module object
    Raises:
        ImportError: when the module can't be loaded
        FileNotFoundError: when module_path doesn't exist
    """
    if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
        import importlib.util

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    elif sys.version_info[0] == 3 and sys.version_info[1] < 5:
        ## SourceFileLoader is also deprecated
        import importlib.machinery

        loader = importlib.machinery.SourceFileLoader(module_name, module_path)
        module = loader.load_module()
    elif sys.version_info[0] == 2:
        ## Deprecated since version 3.4: The imp module is deprecated in favor of importlib.
        import imp

        module = imp.load_source(module_name, module_path)
    return module


version_file = os.path.abspath("pyblish_nuke/version.py")
version_mod = load_module_from_file("version", version_file)
version = version_mod.version


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
    package_data={"pyblish_nuke": ["plugins/*.py", "nuke_path/*.py"]},
    install_requires=["pyblish-base>=1.4"],
)

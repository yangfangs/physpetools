from setuptools import setup, find_packages
from physpetool.version import version

physpe_version = version

try:
    LONG_DESCRIPTION = open("README.rst", "rb").read().decode("utf-8")
except:
    long_descr = "One command auto reconstruct phylogenetic tree"
setup(
    name="PhySpeTree",
    packages=find_packages(),
    entry_points={
        "console_scripts": ['PhySpeTree = physpetool.physpe.physpe:main']
    },
    version=physpe_version,
    description="One command line auto reconstruct phylogenetic tree.",
    long_description=LONG_DESCRIPTION,
    author="Yang Fang",
    author_email="yangfangscu@gmail.com",
    package_data={'': ['*.rst'], 'physpetool': ['database/*.db', 'softwares/*', 'database/*.txt']},
    url="https://github.com/yangfangs/physpetools",
)

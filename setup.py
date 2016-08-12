from setuptools import setup, find_packages
from physpetool.version import version

physpe_version =version

try:
    LONG_DESCRIPTION = open("README.rst", "rb").read().decode("utf-8")
except:
    long_descr = "one command construct species phylogenetic tree "
setup(
    name="physpe",
    packages=find_packages(),
    entry_points={
        "console_scripts": ['physpe = physpetool.physpe.physpe:main']
    },
    version=physpe_version,
    description="Python command line to construct phylogenetic tree.",
    long_description=LONG_DESCRIPTION,
    author="Yang Fang",
    author_email="yangfangscu@gmail.com",
    package_data={'': ['*.rst'], 'physpetool': ['database/*.db', 'softwares/*','database/*.txt']},
    url="https://gitlab.com/xiaoxiaoyang/physpetool/tree/master",
)

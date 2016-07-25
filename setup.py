from setuptools import setup, find_packages

version = "0.1.1"
try:
    LONG_DESCRIPTION = open("README.rst", "rb").read().decode("utf-8")
except:
    long_descr = "one command construct species phylogenetic tree "
setup(
    name="physpe",
    packages=find_packages(),
    entry_points={
        "console_scripts": ['physpe = physpetool.physpe:main']
    },
    version=version,
    description="Python command line to construct phylogenetic tree.",
    long_description=LONG_DESCRIPTION,
    author="Yang Fang",
    author_email="yangfangscu@gmail.com",
    package_data={'': ['*.rst'], 'physpetool': ['database/*.db', 'softwares/*']},
    url="https://gitlab.com/xiaoxiaoyang/physpetool/tree/master",
)

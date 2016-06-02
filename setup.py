from setuptools import setup, find_packages

version = "0.0.8"
# with open("README.rst", "rb") as f:
#     long_descr = f.read().decode("utf-8")
long_descr = "one command construct species phylogenetic tree "
setup(
    name="physpe",
    packages=find_packages(),
    entry_points={
        "console_scripts": ['physpe = physpetool.physpe:main']
    },
    version=version,
    description="Python command line to construct phylogenetic tree.",
    long_description=long_descr,
    author="Yang Fang",
    author_email="yangfangscu@gmail.com",
    package_data={'': ['*.rst'], 'physpetool': ['database/*.db','softwares/*']},
    url="https://gitlab.com/xiaoxiaoyang/physpetool/tree/master",
)

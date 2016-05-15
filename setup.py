from setuptools import setup

version = "0.0.2"
setup(
    name="physep",
    packages=["physeptools"],
    entry_points={
        "console_scripts": ['physeptools = physeptools.physeptools:main']
    },
    version=version,
    description="Python command line to construct phylogenetic tree.",
    long_description="long_descr",
    author="Yang Fang",
    author_email="yangfangscu@gmail.com",
    url="https://github.com/",
)

from setuptools import setup, find_packages

version = "0.0.5"
# with open("README.md", "rb") as f:
#     long_descr = f.read().decode("utf-8")
setup(
    name="physpe",
    packages=find_packages(),
    entry_points={
        "console_scripts": ['physpe = physpetool.physpe:main']
    },
    version=version,
    description="Python command line to construct phylogenetic tree.",
    long_description="long_descr",
    author="Yang Fang",
    author_email="yangfangscu@gmail.com",
    package_data={'': ['*.md'], 'physpetool': ['database/*.db'],
                  'physpetool': ['softwares/*']},
    url="https://gitlab.com/xiaoxiaoyang/physpetool/tree/master",
)

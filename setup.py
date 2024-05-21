from setuptools import setup, find_packages

setup(
    name='tools_slurm',
    version='0.1.6',
    author='Christian Hauschel',
    description='Tools for Slurm automation',
    install_requires=[
        # "pysection @ git+https://github.com/christianhauschel/pysection",
        "rich",
        "quantiphy",
    ],
)
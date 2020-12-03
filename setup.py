import setuptools

tests_dependencies = ["pytest"]
extras = {"test": tests_dependencies}

setuptools.setup(
    name="aoc2020",
    version="0.0.1",
    description="Advent of Code 2020 Solutions",
    author="Vance Morris",
    author_email="vmorris@us.ibm.com",
    packages=setuptools.find_packages(),
    tests_require=tests_dependencies,
    extras_require=extras,
)

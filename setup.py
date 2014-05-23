import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(

        name = "gstar-Google-Play-Scraper",
        description = "Google Play Scraper",
        long_description = read("README"),
        version = "0.1dev",
        py_modules = ["gstar"],

        author = "Justin Jasmann",
        author_email = "justin.jasmann@gmail.com",

        keywords = "",
        license = "BSD",

        install_requires = "beautifulsoup4 >= 4",

    )
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
setup(

        name = "gstar-Google-Play-Scraper",
        long_description = open("README").read(),
        version = "0.1dev",
        packages = ["gstar"],

        author = "Justin Jasmann",
        author_email = "justin.jasmann@gmail.com",

        keywords = "",
        license = "",

        install_requires = "bs4>=4",
        zip_safe = True

    )
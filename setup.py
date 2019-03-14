import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="google-secrets",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",  # example license
    description="A module that generates the credentials.json file for applications that make use of google api using environmental variables",
    long_description=README,
    url="https://www.example.com/",
    author="Biola Oyeniyi",
    author_email="gbozee@gmail.com",
    install_requires=["Click"],
    entry_points = {
        'console_scripts': ['create-google-secrets=g_secrets:create_secrets'],
    },
    dependency_links=[],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: X.Y",  # replace "X.Y" as appropriate
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",  # example license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        # Replace these appropriately if you are stuck on Python 2.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)

"""Python setup.py for flask_template_test package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("flask_template_test", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="flask_template_test",
    version=read("flask_template_test", "VERSION"),
    description="Awesome flask_template_test created by aladecuncun",
    url="https://github.com/aladecuncun/flask-template-test/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="aladecuncun",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["flask_template_test = flask_template_test.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)

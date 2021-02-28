from setuptools import setup, find_packages

setup(
    name="our-vegetable-garden-project",
    version="1.0",
    description="",
    long_description=open("README.md").read(),
    author="Anthony Cox",
    author_email="anthonyjohnc@gmail.com",
    url="undefined",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask"
    ],
)
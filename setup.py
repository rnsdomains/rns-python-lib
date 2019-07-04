import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rns_sdk",
    version="0.0.1",
    author="Gaspar Medina",
    author_email="gmedina@infuy.com",
    description="Python RNS resolver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gasparmedina/rns_sdk_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

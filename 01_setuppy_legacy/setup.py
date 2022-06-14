import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


with open("hello_world/__init__.py", "r") as f:
    for line in f:
        if line.startswith("__version__"):
            ver = line.split("=")[1].strip(' "')


setuptools.setup(
    name="hello_world",
    version=ver,
    author="John Smith",
    description="Hello World setup.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Utilities",
    ],
    packages=["hello_world"],
    install_requires=[],
    licence="GPLv3",
    keywords=["hello", "world"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["hello_world = hello_world.__main__:cli"]},
)

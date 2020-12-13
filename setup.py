import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puffidea",
    version="0.0.1",
    author="puff",
    author_email="angrypuff333@gmail.com",
    description="获取Jetbrains激活码",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PeterPuffer/puffidea",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
import setuptools

setuptools.setup(
    name="puffidea",
    version="0.0.7",
    author="puff",
    author_email="angrypuff333@gmail.com",
    description="获取Jetbrains激活码",
    install_requires=['requests'],
    long_description=open("README.md", 'r').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PeterPuffer/puffidea",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

from setuptools import find_packages, setup

setup(
    name="shit",
    version="0.0.0",
    author="themylogin",
    author_email="themylogin@gmail.com",
    packages=find_packages(),
    scripts=[],
    test_suite="nose.collector",
    url="http://github.com/themylogin/shit",
    description="Git repository for those who don't care",
    long_description=open("README.md").read(),
    install_requires=[],
    setup_requires=[],
)

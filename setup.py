import setuptools
main_ns={}
exec(open('ws/version.py').read(), main_ns)
with open("README.md", "r") as fh:
    long_desc = fh.read()
setuptools.setup(
    name="ws",
    version=main_ns['__version__'],
    author="Ryan J Frizzell",
    author_email="ry.frizzellATgmailDotcom",
    scripts = ["run-ws"],
    description="word search",
    long_description=long_desc,
    url="https://github.com/ryanjfrizzell/ws",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=["ostruct>=2.1.0"],
)

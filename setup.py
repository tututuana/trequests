import setuptools

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setuptools.setup(
    name="trequests",
    author="tututuana",
    description="A faster alternate for the requests library",
    url="https://github.com/tututuana/trequests",
    download_url="https://github.com/tututuana/trequests/archive/refs/heads/main.zip",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=requirements
)

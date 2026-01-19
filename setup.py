import io
import setuptools


with io.open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SoloMicrobe",
    version="0.1.0",
    author="Mekonnen Abyot Melkamu",
    author_email="abyot@pusan.ac.kr",
    description="SoloMicrobe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pnucolab/probe-designer-rtd-tutorial",
    packages=setuptools.find_packages(),
)

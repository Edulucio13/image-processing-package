from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package",
    version="1.0.0",
    author="Eduardo Lucio",
    author_email="edulucio13@gmail.com",
    description="Image processing by NTT Data Engenharia de Dados com Python by Digital Innovation One Inc.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Edulucio13/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)

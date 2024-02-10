import setuptools

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='geo_ng',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.8",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True
)

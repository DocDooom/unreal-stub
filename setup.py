from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")


setup(
    name='unreal_stub',
    version='0.2.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages()
)
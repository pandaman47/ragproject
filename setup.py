from setuptools import setup, find_packages
from pathlib import Path
from typing import List

def get_packages(file_path:str)->List[str]:
    """
    Returns a list of packages from the requirements file.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
            
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='mlragproject',
    version='0.0.1',
    author='Saketh',
    packages=find_packages(),
    ##install_requires=['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn', 'jupyterlab'],
    install_requires= get_packages('requirements.txt'),

    description='A simple ML project template',
    long_description=Path('README.md').read_text(),
)
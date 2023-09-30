from setuptools import find_packages , setup
from typing import List
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n" , "") for i in requirements]

        return requirements
setup(
    name = "DiamondPredictionProject",
    version = '0.0.1',
    author = 'Harsh',
    author_email= 'hs0814497@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages= find_packages()
)
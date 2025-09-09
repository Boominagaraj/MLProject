from setuptools import setup, find_packages

HYPENATE = '-e .'
def get_requirements(file_path):
    '''Read the requirements from a file and return them as a list. '''
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        if HYPENATE in requirements:
            requirements.remove(HYPENATE)
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]




setup(
    name='mlproject',
    version='0.1.0',
    author='Boomi',
    author_email='boominagaraj821@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
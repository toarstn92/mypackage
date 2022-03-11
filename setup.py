from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    package=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/toarstn92/<package-name>',
    author='Adebowale Tosin',
    author_email='adebowale.tosin.e@gmail.com'
)
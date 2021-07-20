from setuptools import setup

setup(
    name='Jerteh',
    version='0.9',
    packages=['Text', 'Noske', 'Utils', 'Unitex', 'Extraction', 'TreeTagger'],
    install_requires=[
        'six==1.16.0',
        'treetaggerwrapper==2.3',
        'tika~=1.24',
        'setuptools~=57.0.0'
    ],
    url='https://github.com/petar-popovic-bg/Jerteh',
    license='GPL',
    author='Petar Popovic',
    author_email='petar.popovic.bg@gmail.com',
    description='Jerteh tools for text processing'
)

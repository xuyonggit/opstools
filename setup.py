from setuptools import setup, find_packages

version = '1.0.0'

if not version:
    raise RuntimeError('Cannot find version information')

install_requires = []
with open('requirements.txt', 'r') as f:
    for req in f.readlines():
        install_requires.append(req.strip())

setup(
    name='opstools2',
    version=version,
    description="opstools2",
    requires=install_requires,
    author='xuyong',
    url='http://xuyongw.com',
    packages=find_packages(exclude=['examples', 'tests']),
    include_package_data=True,
)
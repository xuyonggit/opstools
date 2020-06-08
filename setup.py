from setuptools import setup, find_packages

version = '1.1.1'

if not version:
    raise RuntimeError('Cannot find version information')

install_requires = []
with open('requirements.txt', 'r') as f:
    for req in f.readlines():
        install_requires.append(req.strip())

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='opstools2',
    version=version,
    requires=install_requires,
    author='xuyong',
    author_email='xuyong_bj@163.com',
    url='https://xuyonggit.github.io/opstools2/',
    packages=find_packages(exclude=['examples', 'tests']),
    description="运维工具包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.x',
)
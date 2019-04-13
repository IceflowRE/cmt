#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

# get long description
with Path('README.rst').open(mode='r', encoding='UTF-8') as reader:
    long_description = reader.read()

setup(
    name='CMT',
    version='0.1.0',
    description='Celaria Map Toolkit',
    long_description=long_description,
    author='Iceflower S',
    author_email='iceflower@gmx.de',
    license='MIT',
    url='https://github.com/IceflowRE/cmt',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
    keywords='map toolkit',
    packages=find_packages(include=['cmt', 'cmt.*']),
    python_requires='>=3.7',
    install_requires=[
    ],
    extras_require={
        'dev': [
            'prospector[with_everything]==1.1.6.2',
            'twine==1.12.1',
            'setuptools==41.0.0',
            'wheel==0.33.1',
        ],
    },
    package_data={

    },
    include_package_data=True,
    zip_safe=True,
)

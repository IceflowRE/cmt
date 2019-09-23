#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

# get long description
from cmt import static_data

with Path('README.rst').open(mode='r', encoding='UTF-8') as reader:
    long_description = reader.read()

setup(
    name=static_data.NAME,
    version=static_data.VERSION,
    description=static_data.DESCRIPTION,
    long_description=long_description,
    author=static_data.AUTHOR,
    author_email=static_data.AUTHOR_EMAIL,
    license='MIT',
    url=static_data.PROJECT_URL,
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
            'prospector[with_everything]==1.1.7',
            'pytest==5.1.3',
            'pytest-cov==2.7.1',
            'Sphinx==2.2.0',
            'sphinx-autodoc-typehints==1.8.0',
            'sphinx_rtd_theme==0.4.3',
            'twine==1.15.0',
            'setuptools==41.2.0',
            'wheel==0.33.6',
        ],
    },
    package_data={

    },
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'cmt = cmt.cs.main:main',
        ],
    },
)

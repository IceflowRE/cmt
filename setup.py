#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

from cmt import meta

# get long description
with Path('README.rst').open(mode='r', encoding='UTF-8') as reader:
    LONG_DESCRIPTION = reader.read()

setup(
    name=meta.NAME,
    version=meta.VERSION,
    description=meta.DESCRIPTION,
    long_description_content_type='text/x-rst',
    long_description=LONG_DESCRIPTION,
    author=meta.AUTHOR,
    author_email=meta.AUTHOR_EMAIL,
    license='MIT',
    url=meta.PROJECT_URL,
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
            'flake8>=3.9.2',
            'pylint>=2.11.1',
            'pyroma>=3.2',
            'pytest>=6.2.5',
            'pytest-cov>=2.12.1',
            'setuptools>=58.2.0',
            'Sphinx>=4.2.0',
            'sphinx-autodoc-typehints>=1.12.0',
            'sphinx_rtd_theme>=1.0.0',
            'twine>=3.4.2',
            'wheel>=0.37.0',
        ],
    },
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'cmt = cmt.cs.main:main',
        ],
    },
)

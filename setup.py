from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='mathmatrix',
    packages=['mathmatrix'],
    version='0.2',
    license='MIT',
    description='A package for Python that lets you create and perform various operations on Matrices sucjh as finding the adjoint, inverse, determinant of a matrix, etc..',
    author='Keerthi Vasan S A',
    author_email='sakeerthi23@gmail.com',
    url='https://github.com/Nectres/mathmatrix.git',
    download_url='https://github.com/Nectres/mathmatrix/archive/refs/tags/Alpha.tar.gz',
    keywords=['matrix', 'math', 'mathmatrix', 'matrices', 'matrix inverse',
              'determinant'],
    install_requires=[
        'itertools',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)

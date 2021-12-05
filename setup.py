from distutils.core import setup
setup(
    name='mathmatrix',
    packages=['mathmatrix'],   
    version='0.1',      
    license='MIT',
    description='A package for Python that lets you create and perform various operations on Matrices sucjh as finding the adjoint, inverse, determinant of a matrix, etc..',
    author='Keerthi Vasan S A',
    author_email='sakeerthi23@gmail.com',
    url='https://github.com/Nectres/mathmatrix.git',
    download_url='https://github.com/Nectres/mathmatrix.git/archive/v_01.tar.gz',
    keywords=['matrix', 'math', 'matrices', 'matrix inverse',
              'determinant'],
    install_requires=[
        'itertools',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Math :: Matrices',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Boyer-Moore string search using Cython',
    ext_modules=cythonize('bm_cython.pyx'),
    zip_safe=False
)

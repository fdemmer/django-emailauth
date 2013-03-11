# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

from django_emailauth import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-emailauth',
    version=".".join(map(str, VERSION)),
    description='A user model (with admin) using email as login handle for Django 1.5+',
    long_description=readme,
    author='Florian Demmer',
    author_email='florian@demmer.org',
    url='https://github.com/fdemmer/django-emailauth',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    #test_suite=''
)

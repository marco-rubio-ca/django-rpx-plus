#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='django_rpx_plus',
    #We exclude example app from installing since that may interfere from
    #someone testing out their own example app of the same name. I got
    #bit by this :). We also put django_rpx/ inside of a src/ dir so that
    #installations using 'setup.py develop' don't install example/ (since
    #'setup.py develop' ignores exclude).
    packages=find_packages('src', exclude=['example', 'example.*']),
    package_dir={'' : 'src'},
    include_package_data=True,
    version='2.0.2',
    description='RPX auth support for django',
    author='Michael Huynh',
    author_email='mike@mikexstudios.com',
    license="BSD",
    keywords="janrain django rpx rpxnow",
    url='http://github.com/mikexstudios/django-rpx-plus',
    install_requires=[
        'Django>=1.11',
        'django-picklefield==0.3.2'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ]
)


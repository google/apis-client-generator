#!/usr/bin/python2.7
"""Setup script for Google APIs Client Generator."""

import setuptools


setuptools.setup(
    name='google-apis-client-generator',
    version='1.7.0',
    description='Google Apis Client Generator',
    long_description=open('README').read(),
    author='Google Inc.',
    author_email='opensource-apis-client-generator@google.com',
    url='https://github.com/google/apis-client-generator/',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            ('generate_library = '
             'googleapis.codegen.script_stubs:RunGenerateLibrary'),
            ('expand_templates = '
             'googleapis.codegen.script_stubs:RunExpandTemplates')
            ]},
    include_package_data=True,
    install_requires=['django>=1.11.0, <2.0.0dev',
                      'httplib2>=0.9.2, <2.0.0dev',
                      'google-apputils>=0.4.2, <2.0.0dev',
                      'python-gflags>=2.0, <4.0.0dev',
                      'google-api-python-client>=1.0.0, <2.0.0dev'],
    zip_safe=False)

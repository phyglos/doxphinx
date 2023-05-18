#
# setup.py - Package initialization
#
# Copyright (C) 2018-2023 Angel Linares Zapater
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation. See the COPYING file.
#
# This program is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

import setuptools

# Set README file
long_description = open("README.rst", "r").read()
long_description_content_type="text/x-rst"

setuptools.setup(
    name='doxphinx',
    version='1.x.z',
    license='GPL version 2',
    description='doxphinx for Sphinx',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author='Angel Linares Zapater',
    author_email='alz@phyglos.org',
    url="http://doxphinx.org/",
    project_urls={
        "Documentation": "https://docs.phyglos.org/doxphinx/",
        "Source Code": "https://github.com/phyglos/doxphinx/",
    },
    # packages=setuptools.find_packages(),
    packages=['doxphinx'],
    package_data={
        'doxphinx': [
            'theme.conf',
            '*.html',
            'static/*.*',
            'ext/localtoc/*.*',
        ]
    },
    # include_package_data=True,
    install_requires=['sphinx>=7.0.0'],
    keywords='doxphinx, sphinx, phyglos',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Sphinx :: Extension",
        "Framework :: Sphinx :: Theme",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
     ],
     entry_points = {
         'sphinx.html_themes': [
            'doxphinx = doxphinx',
         ]
     },
 )

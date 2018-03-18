#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2012-2018 Matt Martz
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import re
import codecs

from setuptools import setup


setup(
    name='grasp',
    version='3.7',
    description=('Command line interface for SUAI Timetable'),
    long_description=long_description,
    keywords='grasp suai guap',
    author='Max Sklyarov',
    author_email='maxan9888@gmail.com',
    url='https://github.com/maxan98/grasp',
    license='Apache License, Version 2.0',
    py_modules=['grasp'],
    entry_points={
        'console_scripts': [
            'grasp=grasp:main',
            'timetable-suai=grasp:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
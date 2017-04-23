# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import os


about = {}
about_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'themis', 'finals', 'attack', 'helper', '__about__.py')
with io.open(about_filename, 'rb') as fp:
    exec(fp.read(), about)


setup(
    name='themis.finals.attack.helper',
    version=about['__version__'],
    description='Themis Finals attack helper library',
    author='Alexander Pyatkin',
    author_email='aspyatkin@gmail.com',
    url='https://github.com/themis-project/themis-finals-attack-helper-py',
    license='MIT',
    packages=find_packages('.'),
    install_requires=[
        'setuptools>=35.0.0',
        'requests>=2.11.1',
        'themis.finals.attack.result>=1.3.0,<1.4.0'
    ],
    namespace_packages=[
        'themis',
        'themis.finals',
        'themis.finals.attack'
    ],
    entry_points={
        'console_scripts': [
            'themis-finals-attack = themis.finals.attack.helper:run',
        ]
    }
)

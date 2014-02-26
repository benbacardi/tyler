'''setup.py for tyler'''
from setuptools import setup, find_packages
from tyler.version import __VERSION__

setup(
    name                 = 'tyler',
    version              = __VERSION__,
    description          = 'Python webservice for tiling static maps',
    author               = 'Ben Cardy',
    author_email         = 'benbacardi@gmail.com',
    packages             = find_packages(),
    install_requires     = ['django', 'requests', 'imaging',],
    include_package_data = True,
    classifiers          = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)

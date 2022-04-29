#!/usr/bin/env python3


from setuptools import setup, find_packages


setup(name='monical',
      version='0.0.0',
      scripts=[],
      entry_points={
          'console_scripts': [
              'monical = monical.cmd_monical:main',
          ]
      },
      install_requires=[
          'pygame',
      ],
      packages=find_packages(),
)


# EOF #

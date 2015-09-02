from setuptools import setup, find_packages
import os

version = '0.1'
description = 'Generic Layouts for collective.cover package'
long_description = (
    open('README.txt').read() + '\n' +
    open(os.path.join('docs', 'HISTORY.rst')).read()
)

setup(name='collective.cover.layouts',
      version=version,
      description=description,
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='generic blogs news events e-commerce website layouts collective cover package',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/Covantec/collective.cover.layouts',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.cover'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          # -*- Extra requirements: -*-
          'collective.cover',
      ],
      extras_require={
          'test': [
              'plone.app.robotframework',
              'plone.app.testing [robot] >=4.2.2',
              'plone.browserlayer',
              'plone.testing',
              'robotsuite',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

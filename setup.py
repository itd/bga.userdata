from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='bga.userdata',
      version=version,
      description="Extra user data fields.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='plone, member',
      author='Kurt Bendl',
      author_email='kurt@tool.net',
      url='http://tool.net/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bga'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
)

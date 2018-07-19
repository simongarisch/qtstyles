from setuptools import setup, find_packages

setup(name="qtstyles",
      version="0.0.1",
      install_requires=[
          "QtPy>=1.4.1"
        ],
      description="A collection of Qt style sheets and helpful classes for applying them.",
      long_description=open("README.md").read(),
      include_package_data = True,
      author="Simon Garisch",
      author_email="gatman946@gmail.com",
      packages=find_packages()
     )

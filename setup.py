from setuptools import setup, find_packages

setup(name="qtstyles",
      version="0.0.1",
      install_requires=[
          "QtPy>=1.4.1"
        ],
      description="A collection of Qt style sheets and helpful classes for applying them.",
      long_description=open("README.md").read(),

	  # https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
	  package_data={"qtstyles": ["style_sheets/*.qss"]}, # include style sheets 
      author="Simon Garisch",
      author_email="gatman946@gmail.com",
      url="https://github.com/simongarisch/qtstyles",
      packages=find_packages()
     )

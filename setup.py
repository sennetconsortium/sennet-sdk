from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='sennet-sdk',
      version='0.1',
      description='Schema validating tools',
      url='https://github.com/sennetconsortium/sennet-sdk',
      author='DBMI Pitt',
      license='MIT',
      packages=['ingest_validation_kit', 'ingest_validation_kit.ingest_validation_tools'],
      install_requires=[
        'attrs==21.4.0',
        'certifi==2021.10.8',
        'chardet==4.0.0',
        'click==8.0.4',
        'colorama==0.4.4',
        'decorator==5.1.1',
        'frictionless==4.0.0',
        'idna==2.10',
        'importlib-metadata==4.8.3',
        'isodate==0.6.1',
        'jsonschema==3.2.0',
        'petl==1.7.8',
        'pyrsistent==0.18.0',
        'python-dateutil==2.8.2',
        'python-slugify==6.1.1',
        'pyyaml==6.0',
        'requests',
        'shellingham==1.4.0',
        'simpleeval==0.9.12',
        'six==1.16.0',
        'stringcase==1.2.0',
        'tableschema-to-template==0.0.11',
        'text-unidecode==1.3',
        'typer[all]==0.4.1',
        'typing-extensions==4.1.1',
        'urllib3==1.26.7',
        'validators==0.18.2',
        'xlsxwriter==3.0.3',
        'zipp==3.6.0',
        'setuptools==59.6.0'
      ],
      include_package_data=True,
      package_data={'': ['examples/*', 'ingest_validation_tools/directory-schemas/*', 'ingest_validation_tools/table-schemas/*', 'ingest_validation_tools/error-reports/*', 'ingest_validation_tools/pipeline-infos/*']},
      )
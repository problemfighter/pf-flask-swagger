import os
import pathlib
from setuptools import setup, find_packages

CURRENT_DIR = pathlib.Path(__file__).parent
README = (CURRENT_DIR / "readme.md").read_text()

env = os.environ.get('dev')


def get_dependencies():
    dependency = [
        'Flask',
        'Marshmallow',
        'Apispec',
    ]

    if env and env == "dev":
        return dependency

    return dependency + ["PF-Flask-Rest-Com"]



setup(
    name='PF-Flask-Swagger',
    version='1.0.0',
    url='https://github.com/problemfighter/pf-flask-swagger',
    license='Apache 2.0',
    author='Problem Fighter',
    author_email='problemfighter.com@gmail.com',
    description='Flask Swagger Documentation by Problem Fighter Library',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_dependencies(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
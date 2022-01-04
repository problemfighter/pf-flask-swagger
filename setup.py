from setuptools import setup, find_packages

setup(
    name='PF-Flask-Swagger',
    version='1.0.0',
    url='https://github.com/problemfighter/pf-flask-swagger',
    license='Apache 2.0',
    author='Problem Fighter',
    author_email='problemfighter.com@gmail.com',
    description='Flask Swagger Documentation by Problem Fighter Library',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Marshmallow',
        'Apispec',
    ],
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
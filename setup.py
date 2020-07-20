from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='issue3141',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'z3c.jbot',
    ],
    entry_points='''
        [z3c.autoinclude.plugin]
        target = plone
    ''',
)

from setuptools import setup

setup(
    name='sweepstats',
    version='1.0',
    packages=['sweepstats', 'sweepstats.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        sweepstats=sweepstats.cli:cli
    ''',
)

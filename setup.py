from setuptools import setup

setup(
    name='cliweather_agung',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
        'Requests'
    ],
    entry_points='''
        [console_scripts]
        cliweather=cliweather_agung.main:cli
    ''',
)
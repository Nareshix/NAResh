from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Requests'
    ],
    entry_points={
        'console_scripts': [
            'naresh = package.scripts.naresh:cli',
            'nar = package.scripts.naresh:cli',
        ],
    },
)

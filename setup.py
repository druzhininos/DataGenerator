from setuptools import setup, find_packages

setup(
    name='DataGenerator',
    version='0.1.0',
    description='Parses data schema and generates files with random data',
    author='DruzhininOS',
    author_email='your.email@example.com',
    url='https://github.com/druzhininos/DataGenerator',
    packages=find_packages(),
    install_requires=[
        'uuid',
        'multiprocessing',
        'json',
        'ast',
        'time',
        'random',
        'argparse',
        'configparser',
        'logging'
    ],
    entry_points={
        'console_scripts': [
            'DataGenerator = data_generator.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'
    ]
)

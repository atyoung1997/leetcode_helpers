from setuptools import setup, find_packages

setup(
    name = 'leetcode_helpers',
    version = '0.0.1',
    description = 'tools for running and testing leetcode problems',
    url = 'https://github.com/atyoung1997/leetcode_helpers',
    author = 'adam young',
    
    packages = find_packages(),
    install_requires=[
        'pandas'
    ]
)
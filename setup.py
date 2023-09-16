from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r') as f:
        requirements = f.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]



setup(
    name='tootle',
    version='0.0.1.1',
    include_package_data=True,
    packages=find_packages(exclude=['test', 'test.*']),
    package_data={
        'tootle.dev_bot': ['.autom/*.json'],
    },
    install_requires=read_requirements(),
    author='',
    author_email='',
    description='',
    long_description=open('./README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)

# To build:
# python setup.py sdist bdist_wheel
# To upload to pypi:
# twine upload dist/*

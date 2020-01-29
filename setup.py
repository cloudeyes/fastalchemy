from setuptools import setup
from os import path
this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='fastalchemy',
    packages=['fastalchemy'],
    version='0.1.1',
    license='MIT',
    description='A SQLAlchemy middleware for FastAPI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Joseph Kim',
    author_email='cloudeyes@gmail.com',
    url='https://github.com/cloudeyes/fastalchemy',
    download_url='https://github.com/cloudeyes/fastalchemy/archive/v0.1.1.tar.gz',
    keywords=['fastapi', 'middleware', 'sqlalchemy', 'plugin'],
    install_requires=[
        'fastapi', 'sqlalchemy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)

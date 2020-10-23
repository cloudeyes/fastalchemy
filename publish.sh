#!/bin/bash
rm -f dist/*
python setup.py sdist 
twine upload dist/*

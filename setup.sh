#!/bin/bash

if [ -d "env" ] 
then
    rm -rf env
fi
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
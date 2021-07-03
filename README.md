# stellar
assignment from stellar

# Setup the environment
For the purpose of this project I'm using flask and venv for the API endpoints and environment setup.

For setup -
```
./setup.sh
```
This will create a virtual environment with all requirements installed

To run -
```
(run if env isn't active) source env/bin/activate
python api/api.py
```

To deactivate the virtual environment -
```
deactivate
```

Additional feature -
Added a like API endpoint.

Assumptions -
1. All snippets written to this endpoint can live in memory.

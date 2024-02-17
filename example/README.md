# How to run
- cd to this directory
- `poetry install`
- `poetry shell` to activate virtual environment.  Run `exit` to deactivate.
- Look at `.venv/Lib/`.  Notice a folder called `triangledraw-0.1.0.dist-info` but there is not folder called `triangledraw`.  If poetry install had been performed with `develop = false` then you should also see `triangledraw` in the venv.
- run `python ./example.py`
- Make some change to a source file in `triangledraw`
- run `python ./example.py`.  The behavior of this script should change without needing to reinstall triangledraw.

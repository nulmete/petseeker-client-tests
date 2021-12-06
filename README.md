# Python + Selenium base template

Create a virtual environment: `python -m venv venv`
Activate the venv: `source venv/bin/activate`
Install dependencies: `pip install -r requirements.txt`

Select venv in VSCode:

- CTRL (or Command if using a Mac) + Shift + P.
- Search for `"Python: Select Interpreter"`
- Select the `virtualenv` virtual environment.

# Run tests

- `pytest -s .\tests\test_publications.py --settings=settings.development`

## setup venv

To setup venv please in the project root run:

```
python -m venv ~/.virtualenvs/datura
pip install -r ./requirements.txt
```

## run tests
```
PYTHONPATH=. pytest ./src/tests.py
```

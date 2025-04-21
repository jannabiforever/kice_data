# Kice Data

data reformation on KICE datum.

## Data explanation

png/* : png files of pages.
pdf/* : raw pdf files of KICE.
schema.json: map of each problem to page index and image box. (to be cropped!)

## Run
You can obtain the problem datum by running command:

```bash
python -m venv .venv
pip install -r requirements.txt
python main.py
```

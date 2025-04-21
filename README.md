# Kice Data

data reformation on KICE datum.
you can also get pdfs from [KICE](https://www.suneung.re.kr/boardCnts/list.do?boardID=1500234&m=0403&s=suneung&searchStr=)

## Data explanation

png/* : png files of pages.<br>
pdf/* : raw pdf files of KICE.<br>
schema.json: map of each problem to page index and image box. (to be cropped!)<br>

## Run
You can obtain the problem datum by running command:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

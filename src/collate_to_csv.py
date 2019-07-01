#!/usr/bin/env python
import csv
from pathlib import Path
from xlrd import open_workbook
SRC_DIR = Path('data/parsed/abbyy')

for fn in SRC_DIR.glob('20*.xlsx'):
    destname = SRC_DIR / (str(fn.stem) + '.csv')
    print(destname)
    with open(destname, 'w') as w:
        sheet = open_workbook(fn).sheets()[0]
        o = csv.writer(w)
        o.writerows(sheet.row_values(i) for i in range(sheet.nrows))

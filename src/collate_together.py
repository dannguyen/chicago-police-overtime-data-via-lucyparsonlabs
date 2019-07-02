#!/usr/bin/env python
import csv
import json
from pathlib import Path
import re
from xlrd import open_workbook
SRC_DIR = Path('data/parsed/abbyy')
DEST_DIR = Path('data/collated')


def collate_aggregates():
    data = []
    for fn in SRC_DIR.glob('*aggregate.csv'):
        year = re.match(r'^\d{4}', fn.name)[0]
#        print(year, fn)
        # data looks like:
        # April,MONEY,TIME,TOTAL ACT HRS,TOTAL CRED HRS,TOTAL AMT
        # ,"106,405.50","18,633.75",127911.50,"186,569.86","8,308,801.95"
        lines = list(csv.reader(fn.read_text().splitlines()))
        for rows in [lines[i:i+2] for i in range(0, len(lines), 2)]:
            headers, vals = rows
            d = { 'year': year, 'month': headers[0],}
            for i, v in enumerate(vals[1:]):
                d[headers[i+1]] = v
            data.append(d)

    destname = DEST_DIR / 'cpd-overtime-aggregate.csv'
    with open(destname, 'w') as w:
        o = csv.DictWriter(w, fieldnames=data[0].keys())
        o.writerows(data)
    print( destname)


def collate_units():
    data = []
    for fn in SRC_DIR.glob('*by-unit.csv'):
        year = re.match(r'^\d{4}', fn.name)[0]
#        print(year, fn)
        # data looks like:
        # April,MONEY,TIME,TOTAL ACT HRS,TOTAL CRED HRS,TOTAL AMT
        # ,"106,405.50","18,633.75",127911.50,"186,569.86","8,308,801.95"
        lines = list(csv.reader(fn.read_text().splitlines()))
        for rows in [lines[i:i+2] for i in range(0, len(lines), 2)]:
            headers, vals = rows
            d = { 'year': year, 'month': headers[0],}
            for i, v in enumerate(vals[1:]):
                d[headers[i+1]] = v
            data.append(d)

    destname = DEST_DIR / 'cpd-overtime-aggregate.csv'
    with open(destname, 'w') as w:
        o = csv.DictWriter(w, fieldnames=data[0].keys())
        o.writeheader()
        o.writerows(data)
    print( destname)



def main():
    collate_aggregates()

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""MHC-Peptide-Pairer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16byNiV536xLeJT7R8IHNwOM7UKdsGRDE
"""

import argparse
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument("--list", nargs="+")
value = parser.parse_args()
listpep = value.list

mhc = listpep[0]
peptide = listpep[1]

mhc_dict = {
    'Mamu-B5201': 'Mamu-B52',
    'Mamu-A0201': 'Mamu-A02',
    'Mamu-B0101': 'Mamu-B:00101',
    'Mamu-B0301': 'Mamu-B:00301',
    'Mamu-B0401': 'Mamu-B:00401',
    'Mamu-A070103': 'Mamu-A7:0103',
    'Mamu-B1701': 'Mamu-B17',
    'Mamu-A1101': 'Mamu-A11',
    'Mamu-A020102':'Mamu-A2:0102',
    'Mamu-B0801': 'Mamu-B008:01',
    'Mamu-A0101': 'Mamu-A01',
    'Mamu-B6502': 'Mamu-B:06502',
    'BoLA-HD:00601': 'BoLA-HD6'
}
def mhc_rename(mhc):
    mhc = mhc.replace(':', '')
    if mhc[:4] == 'BoLA':
        mhc = mhc.replace('*', ':0')
    else:
        mhc = mhc.replace('*', '')

    if mhc in mhc_dict:
        mhc = mhc_dict[mhc]

    return mhc

mhc = mhc_rename(mhc)
output_list = [mhc,peptide]
df = pd.DataFrame(output_list)
df.to_csv('pair.csv', index=False)

stringwrite = mhc+','+peptide
print(stringwrite)

file = open("/content/DeepLigand-master/examples/singleexample", "w") 
file.write(stringwrite) 
file.close()
from numpy import nan
from numpy import isnan
import pandas as pd
from pandas.core.dtypes.missing import notnull

def calculate_budget(exelData):
    data = fillData(exelData)
    return data
    

def fillData(path):
    data = {}
    doc = pd.read_excel(path, sheet_name=0)
    ids = []
    first = True
    parsedoc = doc.values.tolist()
    for line in parsedoc:
        name = line[0]
        c1 = line[2]
        c2 = line[3]
        id = str(line[1])
        id = id.replace(' ', '')
        if id in ids:
            if (path == 'Факт - 2012.xlsx'):
                c1 = line[3]
                c2 = line[4]
                id = str(line[2])
            if del_nulls:
                pass
                
                id = id[3:]
            if not isnan(c1) and not isnan(c2):
                if first:
                    data.update({id:[line[0], c1, c2]})
                elif id in data.keys():
                    data[id].append(c1)
                    data[id].append(c2)
                    t = data[id]

def clearNotFull():
    for i in data.keys():
        r = data[i]
        len = r.__len__()
        if (len == 21):
            resultData.update({i:r})
    pass
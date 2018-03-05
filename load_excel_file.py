#load excel-file

import cfg
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def load_xlsx():
    '''Open excel file and prepare to work'''
    
    cfg.work_file = pd.read_excel('Управление_зонами_пикинга.xlsx', sheet_name='Отчет 1')
    cfg.work_file = cfg.work_file.rename(columns=lambda x: x.strip().replace(' ','_')) #delete empty spaces in columns

    print("Column headings: ")
    print(cfg.work_file.columns) # print headers of sheet
    cfg.work_file = cfg.work_file.dropna(subset=['No_vague']) # delete NaN rows in column
    cfg.work_file['No_vague'] = cfg.work_file['No_vague'].apply(int) # change datatype to int64 for column
    print(cfg.work_file['No_vague'].unique())
    cfg.work_file = cfg.work_file.reset_index(drop=True)
    cfg.list_w = cfg.work_file['No_vague'].unique().tolist() # create list with unique values
    
    return cfg.list_w
    return cfg.work_file

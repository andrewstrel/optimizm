import cfg
from tkinter import *
from load_excel_file import *
import tkinter.ttk as ttk

root = Tk()
root.geometry('1800x900+10+5')
scrollbar = Scrollbar(root)


def analyzing():
    '''Load .xlsx file and add to list_of_waves'''
    load_xlsx()
    list1 = cfg.list_w
    for i in list1:
        list_of_waves.insert(END, i)

def optim():
    list2 = [list_of_waves.get(idx) for idx in list_of_waves.curselection()]    
    for i in list2:
        list_of_choise.insert(END, i)

    cfg.choise_wave = list2
    return cfg.choise_wave

def get_magick():
    '''Delete waves which not in cfg.choise_wave'''
    cfg.work_file = cfg.work_file[cfg.work_file['No_vague'].isin(cfg.choise_wave)]
    print(cfg.work_file['No_vague'])
    
bt_load = Button(root, text='Загрузить файл', width=15, height=3, command=analyzing)
bt_load.grid(row=0, column=0, padx=4, pady=2)

list_of_waves = Listbox(root, height=5, width=15, yscrollcommand=scrollbar.set, selectmode=EXTENDED)
list_of_waves.grid(row=1, column=0)
scrollbar.config(command=list_of_waves.yview)

bt_choise = Button(root, text='Выбрать волну', width = 15, height=3, command=optim)
bt_choise.grid(row=2, column=0, padx=4, pady=2)

list_of_choise = Listbox(root, height=5, width=15, yscrollcommand=scrollbar.set, selectmode=EXTENDED)
list_of_choise.grid(row=3, column=0)

#delete items from list_of_choise
list_of_choise.bind('<Double-1>', lambda x: list_of_choise.delete(ACTIVE))

bt_magick = Button(root, text='Сделать красиво', width=15, height=3, command=get_magick)
bt_magick.grid(row=4, column=0, padx=4, pady=2)

stations = ttk.Treeview(root, selectmode='none')
stations.grid(row=0, rowspan=150, column=2, columnspan=350, padx=5, ipadx=720, ipady=320, sticky='nsw')

vad_01 = stations.insert('', END, text='VAD-01')
vad_01_table = stations.insert(vad_01, END)
vad_02 = stations.insert('', END, text='VAD-02')
vad_02_table = stations.insert(vad_02, END)
vad_03 = stations.insert('', END, text='VAD-03')
vad_03_table = stations.insert(vad_03, END)
vad_04 = stations.insert('', END, text='VAD-04')
vad_04_table = stations.insert(vad_04, END)
vad_05 = stations.insert('', END, text='VAD-05')
vad_05_table = stations.insert(vad_05, END)
vad_06 = stations.insert('', END, text='VAD-06')
vad_06_table = stations.insert(vad_06, END)
vad_07 = stations.insert('', END, text='VAD-07')
vad_07_table = stations.insert(vad_07, END)
vad_08 = stations.insert('', END, text='VAD-08')
vad_08_table = stations.insert(vad_08, END)

root.mainloop()

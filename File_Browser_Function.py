# Author: Thomas Shetler
#
# purpose: to challenge my self and transfer text files to a different folder
#
#
#
#
#
#
#
#

import time
import os

from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import shutil
import File_Browser_GUI
import File_Browser_Main


def center_window(self, w, h):
    # pass in the Tkinter main frame
    # get users height and width
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit Application?"):
        # this closes app
        self.master.destroy()
        os._exit(0)


def ask_source(self, e=None):
    self.src = askdirectory()
    self.srcEntryBox.set(self.src)
    self.path_source = self.srcEntryBox.set(self.src)


##asks for source location and set the name oif the file


def create_db(self):
    conn = sqlite3.connect('db_log.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_log( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_filename TEXT, \
                    col_date TEXT \
                    );")
        conn.commit()
    conn.close()
    first_run(self)



def ask_destination(self, e=None):
    self.des = askdirectory()
    self.desEntryBox.set(self.des)
    self.path_dest = self.desEntryBox.set(self.des)


def list_directory(self):
    entrySrc = self.src
    entryDes = self.des
    dirs = os.listdir(str(entrySrc))
    fileToTransfer = []
    ##looks for file in directory
    for file in dirs:
        if file.endswith("txt"):
            src = ("{}\\{}".format(entrySrc, file))
            var_filename = file
            var_date = os.path.getmtime(src)
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(var_date))
            print(file)
            ##adds file to array (not really used but could be useful later)
            fileToTransfer = fileToTransfer + [file]
            ##moves file from first folder to second folder
            shutil.move(src, entryDes)
            conn = sqlite3.connect('db_log.db')
            ##puts the data into a data base
            with conn:
                cursor = conn.cursor()

                cursor.execute("""INSERT INTO tbl_log (col_filename,col_date) VALUES (?,?)""",
                               (var_filename, modificationTime))
                conn.commit()
            conn.close()


def first_run(self):
    conn = sqlite3.connect('db_log.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_log (col_filename, col_date) VALUES (?,?)""",
                        ('blank.txt', '1/01/1'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_log""")
    count = cur.fetchone()[0]
    return cur, count


if __name__ == "__main__":
    pass

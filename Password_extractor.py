#!/bin/python3
import os
import threading
import re
from string import printable
import sys

directory = input("Please enter the location of breach:")
symbol = input("Please enter the seperating symbol:")


def valid_dir(Dir):
    is_dir = os.path.exists(Dir)
    if is_dir == True:
        print("The directory exists.")
    else:
        print("Please enter a valid directory")
        print("Exiting...")
        sys.exit()


def list_dirs(directory):
    dir_list = []
    for (dirpath, dirname, filename) in os.walk(directory):
        for file in filename:
            dir_list.append(os.path.join(dirpath, file))
    return dir_list


def finding_master():
    files = os.listdir()
    master_pass = False
    for file in files:
        if file == "master_pass.txt":
            master_pass = True
            break
    if master_pass == False:
        fh = open("master_pass.txt", "w")
        fh.close()


def reading_data(location):
    print(location)
    raw_data = open(location)
    for each_line in raw_data:
        line = utf(each_line)
        if line == False:
            pass
        else:
            password = parsing_data(each_line, symbol)
            storing_output(password)
    raw_data.close()
    success_read(location)




def success_read(location):
    fh = open("Files_read.txt", "a")
    fh.write(f"{location}\n")
    fh.close()


def parsing_data(line, seperator):
    password = str(line)
    password = password.split(str(seperator))
    password = password[len(password)-1]
    return password


def utf(string_to_check):
    ASCII = True
    for c in string_to_check:
        if c not in printable:
            ASCII = False
        else:
            pass
    if ASCII == True:
        return string_to_check
        # parsing_data(each_line, symbol)
        # storing_output(string_to_check)
    else:
        return False


def storing_output(passw):
    if len(passw) >= 9:
        fh_eight = open("password_8_above", "a")
        fh_eight.write(passw)
        fh_eight.close()
    elif len(passw) == 5:
        fh_four = open("password_4.txt", "a")
        fh_four.write(passw)
        fh_four.close()
    elif len(passw) > 5 and len(passw) < 9:
        fh_foeit = open("password_4_8.txt", "a")
        fh_foeit.write(passw)
        fh_foeit.close()


def files_read(all_files):
    fh = open("Files_read.txt", "r")
    fh_read = fh.read()
    file_to_read = []
    for i in all_files:
        if i not in fh_read:
            file_to_read.append(i)
    fh.close()

    return file_to_read


valid_dir(directory)
list_of_files = list_dirs(directory)
files_to_read = files_read(list_of_files)

files_to_read.sort()

print("These are all of the files to be scanned.")
for i in range(len(list_of_files)):
    print(f"{i+1}+++{list_of_files[i]}")

print("These are all of the files to be read.")
for i in range(len(files_to_read)):
    print(f"{i+1}>>>{files_to_read[i]}")

for i in files_to_read:
    reading_data(i)

"""This module provides functions for creating series of projects forlders"""

import pathlib
import time

"""Creat folders for a given range of years."""
def create_folders_for_range(Start, end):
    
    for year in range (Start, end + 1 ):
         folder_path = pathlib.Path(f'year_{year}')
         folder_path.mkdir(exist_ok=True)


"""create forlders from list of names."""
def create_folders_for_list(folders_list):
     
     for folder_name in folders_list:
          folder_path = pathlib.Path(folder_name)
          folder_path.mkdir(exist_ok=True)


"""Create Prefixed folders"""
def create_prefixed_folders(folders_list, prefix):
     
    for item in folders_list: 
          folder_path = pathlib.Path(f'{prefix}{item}')
          folder_path.mkdir(exist_ok=True)


"""Creat folders periodically using a while loop"""
def create_folders_periodically(duration):
    
     counter=0
     while counter<5:
          folder_path = pathlib.Path(f'Folder_{counter}')
          folder_path.mkdir(exist_ok=True)
          counter += 1
          time.sleep(duration)

def main ():
     """Main function to demostrate module is capabilities"""

     create_folders_for_range(2020,2024)
     folder_names = ['data-csv', 'data-excel,' 'data-json']
     create_folders_for_list(folder_names)
     prefix = 'data-'
     create_prefixed_folders(folder_names, prefix)

     create_folders_periodically(5)

if __name__== '__main__':
    main()
     

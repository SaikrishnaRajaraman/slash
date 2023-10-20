"""
Copyright (C) 2023 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: slashse2023@gmail.com

"""
import csv
from datetime import datetime
import os


def write_csv(arr,product,file_path):
	''' Returns the CSV file with the naming nomenclature as 'ProductDate_Time'
        Parameters- product: product entered by the user, file_path: path where the csv needs to be stored
        Returns- file_name: CSV file '''
	os.chdir(file_path)
	keys = arr[0].keys()
	now=datetime.now()
	file_name=product+now.strftime("%m%d%y_%H%M")+'.csv'
	a_file = open(file_name, "w", newline='')
	dict_writer = csv.DictWriter(a_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(arr)
	a_file.close()
	return file_name

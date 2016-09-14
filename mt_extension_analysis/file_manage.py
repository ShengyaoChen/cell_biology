import os
import re
from shutil import copy

# os.makedirs('folder_for_images_analysis')

file_list = os.listdir(os.getcwd())
extension_list = [i for i in file_list if i[-3:] == 'tif' and i[:7] != 'Drawing']
print(extension_list)


seed_list = []
for i in extension_list:
	ex_digit = re.findall(r'\d+', i)[-1]
	try:
		temp = i.split(ex_digit + '.tif')[0] + str(int(ex_digit) - 1) + '.tif'
		seed_list.append(temp)
	except Exception as e:
		print(e)
		pass

print('seed_list: ', seed_list)

os.chdir('seeds')
for i in seed_list:
	try:
		copy(i, '..')
	except Exception as e:
		print(e)

print('finished')

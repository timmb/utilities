#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import os, datetime, subprocess, PIL
from PIL import Image

dry_run = False

# if not os.name == 'nt' and not dry_run:
	# raise Exception('This script can only be run on Windows for now')

move_command = 'move' if os.name == 'nt' else 'mv'

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

ls = os.listdir('.')
for entry in ls:
	if (os.path.isfile(entry) 
		and entry 
		and entry[0] != '.' 
		and any([entry.lower().endswith(x) for x in ('jpg', 'jpeg', 'cr2', 'raf', 'xmp', 'psd', 'xml', 'arw', 'mp4')])
		):
		date = datetime.datetime.fromtimestamp(os.stat(entry)[8])
		datestring = '{}-{:02}-{:02}'.format(date.year, date.month, date.day)
		print(f'creating directory: {datestring}')
		if dry_run:
			print(f'os.makedirs({datestring}, exist_ok=True)')
		else:
			os.makedirs(datestring, exist_ok=True)
		dest = '{}/{}'.format(datestring, entry)
		# shutil.move(entry, dest)
		print("{} -> {}".format(entry, dest))
		if dry_run:
			print(f"""subprocess.call(f'{move_command} "{entry}" "{dest}"', shell=True)""")
		else:
			subprocess.call(f'{move_command} "{entry}" "{dest}"', shell=True)
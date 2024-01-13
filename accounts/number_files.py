#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import shutil, os, datetime

def number_files(files, first_number, prefix='R', dry_run=False, base_path="."):
	'''Rename the files in the list putting the prefix and number at the start.

	e.g. number_files(['file.pdf', 'another.pdf'], 24)
	Renames: 'file.pdf' -> 'R24 file.pdf'
	Renames: 'another.pdf' -> 'R25 another.pdf'
	'''
	for i, file in enumerate(files):
		path = '{}/{}'.format(base_path, file)
		out_path = '{}/{}{} {}'.format(base_path, prefix, first_number + i, file)
		print("{} -> {}".format(path, out_path))
		if not dry_run:
			shutil.move(path, out_path)

def get_files(extensions=["pdf"]):
	'''Returns files with the given extensions'''
	ls = os.listdir('.')
	return sorted([p for p in ls if 
		p and 
		p[0] != '.' and 
		os.path.splitext(p)[1][1:] in extensions
		], key=os.path.getctime)

def number_pdf_files(first_number, extensions=["pdf"], dry_run=False):
	'''Searches for files with given extensions and renames them <Rxxx filename>
	counting up from first_number.'''
	filenames = get_files(extensions)
	number_files(filenames, first_number, 'R', dry_run)

def get_first_number_from_user():
	number = None
	while type(number) is not int or number < 0 or number > 100000:
		if number is not None:
			print("Entry needs to be an integer between 0 and 100000.")
		try:
			number = int(input("Enter first receipt number: "))
		except ValueError as e:
			print(e)
	return number


if __name__ == '__main__':
	first_number = get_first_number_from_user()
	assert(type(first_number) is int)
	number_pdf_files(first_number, dry_run=True)
	should_continue = input("\n*** Files will be renamed as above. Enter Y to continue: ")
	if should_continue in ('y','yes','Y','YES','Yes'):
		print('Proceeding with rename...')
		number_pdf_files(first_number, dry_run=False)
		print("\n*** Rename complete.")
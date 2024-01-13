#! /usr/bin/env python3

# Requires pip3 install python-dateutil

import os, datetime, shutil, re
from dateutil.parser import parse

root_dir = os.path.dirname(os.path.realpath(__file__))

pattern = r'^((.*), )?(\d\d? \w+ \d\d\d\d)$'
verbose = False

renames = []

print(f'Searching {root_dir}...')
ls = os.listdir(root_dir)
if len(ls)==0:
    print('Nothing found in directory')
for entry in ls:
    if (not os.path.isdir(entry)):
        continue

    original = entry
    match = re.search(pattern, original)
    if not match or len(match.groups()) != 3:
        if verbose:
            print(f'Failed to find date in string "{entry}". match: "{match.groups() if match else None}"')
        continue
        
    description = match.group(2)
    formatted_date = match.group(3)
    try:
        date = parse(formatted_date)
    except ValueError:
        print(f'Failed to parse date from "{formatted_date}".')
        continue

    new_date = date.date().isoformat()
    if description is None:
        new_name = new_date
    else:
        new_name = f'{new_date} {description}'
    print(f'"{original}" -> "{new_name}"')
    renames.append((original, new_name))

input("Press Enter to continue...")
for original_name, new_name in renames:
    os.system(f'mv "{original_name}" "{new_name}"')
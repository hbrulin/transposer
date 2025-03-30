import csv
import sys
import webbrowser
import os
import const
from tools import is_not_csv
from tools import parse
from tools import split_camel_case
from logic import transpose
from genhtml import generate_html

# check arg
if len(sys.argv) != 2 or is_not_csv(sys.argv[1]):
    print("Usage: python script.py file.csv")
    sys.exit(1)
file = sys.argv[1]  

title = split_camel_case(file)
print(title)

l = []
r = []

# open file
with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['source'] not in const.note_to_midi:
            print(row['source'], row['dest'] if row.get('dest') else "")
            l.append(row['source'])
            r.append(row['dest']) if row.get('dest') else r.append("---------------")
            continue
        s_key, d_key, ls_notes, rs_notes = parse(row)
        ld_notes = transpose(s_key, d_key, ls_notes)
        rd_notes = transpose(s_key, d_key, rs_notes)
        print("\033[34m" + " ".join(ld_notes) + "\033[0m")
        print("\t\033[31m" + " ".join(rd_notes) + "\033[0m")
        l.append(ld_notes)
        r.append(rd_notes)

filename = generate_html(title, d_key[0], l, r)

# Open in web browser with absolute path
filepath = os.path.abspath(filename)
webbrowser.open(f"file://{filepath}")
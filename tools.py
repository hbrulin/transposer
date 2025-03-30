import const
import re 

def split_camel_case(text):
    text = text.replace(".csv", "")
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    result = result.title()
    return result

#Check csv file input
def is_not_csv(file):
    return not file.lower().endswith('.csv')

# Parse my file
def parse(row):
    s_key = const.scales[row['source']]
    d_key = const.scales[row['dest']]
    ls_notes = row['l_notes'].split(" ")
    rs_notes = row['r_notes'].split(" ")
    return s_key, d_key, ls_notes, rs_notes
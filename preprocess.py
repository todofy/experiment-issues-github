import sys
import csv
import json

input = "./data.csv"
output = "./data/data.csv"

ofp = open(output, 'w', encoding='utf8')
writer = csv.writer(ofp, dialect='excel', lineterminator='\n')

header = ['repo_id', 'repo_name', 'id', 'title', 'body',
            'created_by', 'created_at', 'updated_at',
            'closed_at', 'state', 'n_comments', 'locked',
            'milestone', 'labels']
rows = []

# read the file line by line and dump it to csv
with open (input, 'r', encoding='utf8') as ifp:
    for i, _line in enumerate(ifp):
        obj = json.loads(_line)
        if not obj['repo_name'] == "phpmyadmin/phpmyadmin":
            continue

        # add labels to dataset
        labels = []
        if 'labels' in obj and len(obj['labels']) > 0:
            for label in obj['labels']:
                labels.append(label['name'])
        labels = " ".join(labels)

        rows.append([obj['repo_id'], obj['repo_name'], obj['id'],
                    obj['issue'],obj['body'], obj['user'], obj['created_at'],
                    obj['updated_at'], obj['closed_at'], obj['state'],
                    obj['comments'], obj['locked'], obj['milestone'],
                    labels])

## PREPROCESSING TASK 1: retrieve actual author
import re
regex = r".*\*\*Original\sauthor\*\*\:\s([a-zA-Z0-9\-\.\_\*]*)"
header.append('actual_author')
row_modified = []
for row in rows:
    if row[5] == 'pma-import':
        # retrieve the author name from body
        matches = re.finditer(regex, row[4])
        actual_author = None
        for match in matches:
            actual_author = (match.groups()[0])
            break
        if not actual_author:
            print ("AA NOT FOUND")
            print (row[4])
            sys.exit()
        row.append(actual_author)
    else:
        row.append(row[5])
    row_modified.append(row)


# write header to output
writer.writerow(header)

# write each row to csv
# TODO: deduplication by code itself?
for row in row_modified:
    writer.writerow(row)

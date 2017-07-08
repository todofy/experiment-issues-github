import sys
import csv
import json

input = "./data.csv"
output = "./data/data.csv"

ofp = open(output, 'w', encoding='utf8')
writer = csv.writer(ofp, dialect='excel', lineterminator='\n')
# write header to output
writer.writerow(['repo_id', 'repo_name', 'id', 'title', 'body',
                'created_by', 'created_at', 'updated_at',
                'closed_at', 'state', 'n_comments', 'locked', 'milestone'])

# read the file line by line and dump it to csv
with open (input, 'r', encoding='utf8') as ifp:
    for i, _line in enumerate(ifp):
        obj = json.loads(_line)
        if not obj['repo_name'] == "phpmyadmin/phpmyadmin":
            continue

        writer.writerow([obj['repo_id'], obj['repo_name'], obj['id'],
                    obj['issue'],obj['body'], obj['user'], obj['created_at'],
                    obj['updated_at'], obj['closed_at'], obj['state'],
                    obj['comments'], obj['locked'], obj['milestone']])

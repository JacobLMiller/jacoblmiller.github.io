import pybtex
from pybtex.database import parse_file

res = parse_file("pubs.bib")

for entry in list(res.entries.values()):
    print(entry.fields['year'])
    print(entry.to_string('bibtex'))
"""
Iterate over a MARC file, print out all title.

Example input file: https://is.gd/QUNyGk

    $ make clean && make
    $ python app.zip catalog.mrc | grep -i london
"""

import pandas as pd
import pymarc
import random
import sys

location = [
    "Campus",
    "Albertina"
]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: %s FILE' % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1], 'rb') as handle:
        reader = pymarc.MARCReader(handle,
                                   to_unicode=True,
                                   force_utf8=False)
        data = []
        for record in reader:
            title = record.title()
            data.append([title, random.choice(location)])

    df = pd.DataFrame(data)
    df.to_excel("output.xlsx")


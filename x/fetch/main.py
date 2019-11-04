#!/usr/bin/env python
#
# https://sigel.staatsbibliothek-berlin.de/api/hydra/?q=*
#
# {
#       "@context": "https://sigel.staatsbibliothek-berlin.de/typo3conf/ext/zdb_json_api/Resources/Public/context.jsonld",
#       "id": "https://sigel.staatsbibliothek-berlin.de/api/hydra/?q=%2A",
#       "type": "Collection",
#       "freetextQuery": "*",
#       "totalItems": 17735,
#
#  "view": {
#    "type": "PartialCollectionView",
#    "id": "https://sigel.staatsbibliothek-berlin.de/api/hydra/?q=%2A&page=1",
#    "totalItems": 10,
#    "pageIndex": 1,
#    "numberOfPages": 1774,
#    "offset": 1,
#    "limit": 10,
#    "first": "https://sigel.staatsbibliothek-berlin.de/api/hydra/?q=%2A&page=1",
#    "last": "https://sigel.staatsbibliothek-berlin.de/api/hydra/?q=%2A&page=1774",
#    "next": "https://sigel.staatsbibliothek-berlin.de/api/hydra/?q=%2A&page=2"
#  },
#

import requests
import sys

OUTFILE = "data.json"

with open(OUTFILE, "w") as output:

    # Variablezuweisung
    page = 1

    # Schleife (endlos)
    while True:

        # Zuweisung
        url = "https://sigel.staatsbibliothek-berlin.de/api/hydra/?page={}&q=*".format(page)

        # Print
        print(url, file=sys.stderr)

        # Variablenzuweisung
        resp = requests.get(url)
        if resp.status_code >= 400:
            raise RuntimeError('got %s on %s', resp.status, url)

        # Variablenzuweisung
        doc = resp.json()

        # Aufruf
        output.write(resp.text)
        output.write("\n")

        # Variablenzuweisung
        total = doc["view"]["numberOfPages"]

        # Print
        print("{} / {}".format(page, total), file=sys.stderr)

        # Bedingung / Vergleich
        if page == total:
            break

        # Variablenzuweisung
        page += 1
main()


#!python3
# -*- coding: utf-8 -*-

"""
This is

"""
import logging
import numpy as np
import re
import time
import argparse
import sys
import pandas as pd
from pathlib import Path



def extract_abstract(tex):
    info = re.findall(r'\\begin{abstract}(.*?)\\end{abstract}', tex, re.S)
    if len(info) == 1:
        return info[0]
    elif len(info) > 1:
        logging.error("Multiple matches")
        sys.exit(1)
    else:
        return ""

def index_info(authors):
    res = [a.rsplit(maxsplit=1) for a in re.split(r",| and ", authors)]
    idxinfo = " ".join(["\index[authors]{%s, %s}"%(ln, fn) for (fn,ln) in res])
    return idxinfo

def get_latex(template, title, authors, abstract):
    # Process authors for the index
    template = re.sub("__TITLE__", lambda x: title, template)
    template = re.sub("__AUTHORS__", lambda x: authors, template)
    template = re.sub("__INDEXINFO__", index_info(authors), template)
    # the following avoids interpreting escaped chars in the abstract, such as \and
    template = re.sub("__ABSTRACT__", lambda x: abstract, template)
    return template

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Extracts info from TeX file')
    PARSER.add_argument("-debug", action='store_true', default=False, help="Turns on debug information")
    PARSER.add_argument("-toc", dest="toc", default="metadata/toc.tsv", help="file containing the ref, title, and authors")
    PARSER.add_argument("-template", dest="template", default="metadata/subfile.template", help="File containing the TEX template")
    #PARSER.add_argument("-abstract", dest="abstract", default=None, help="File containing the abstract")
    PARSER.add_argument("-outdir", dest="outdir", default=None, help="Output directory")
    PARSER.add_argument("files", nargs='*', help='List of files containing the abstracts')
    args = PARSER.parse_args()

    if args.debug:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    if args.toc:
        toc = pd.read_csv(args.toc, encoding="utf-8", sep='\t', index_col="Ref")

    if args.template:
        with open(args.template, "r", encoding="utf-8") as f:
            template = "".join(f.readlines())

    if len(args.files) > 0:
        for fname in args.files:
            id = int(Path(fname).stem)  # gets the file ID
            logging.debug("Ref: {}".format(id) )
            logging.debug("{}: ({}) ({})". format(id, toc.loc[id]["authors"], toc["title"][id]) )

            with open(fname, "r", encoding="utf-8") as f:
                abstract = "".join(f.readlines())

            result = get_latex(template, toc["title"][id], toc.loc[id]["authors"], abstract)

            if args.outdir is not None:
                with open("{}/{}.tex".format(args.outdir, id), "w", encoding="utf-8") as f:
                    f.write(result)
                logging.info("Wrote {}/{}.tex".format(args.outdir, id))
            else:
                print(result)



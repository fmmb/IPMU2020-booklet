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

class clock():
    def __init__(self):
        self.start_time = time.time()

    def elapsed(self, msg=""):
        logging.info("[%.2fs] %s" % ( time.time() - self.start_time, msg ))

def extract_abstract(tex):
    info = re.findall(r'\\begin{abstract}(.*?)\\end{abstract}', tex, re.S)
    if len(info) == 1:
        return info[0]
    elif len(info) > 1:
        logging.error("Multiple matches")
        sys.exit(1)
    else:
        return ""

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Extracts info from TeX file')
    PARSER.add_argument("-debug", action='store_true', default=False, help="Turns on debug information")
    #PARSER.add_argument("-oprefix", dest="oprefix", default=None, help="Output file name prefix")
    # PARSER.add_argument("-epochs", type=int, default=10, help="Number of training epochs")
    PARSER.add_argument("files", nargs='*', help='List of tex files to use')
    args = PARSER.parse_args()

    if args.debug:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    #T = clock()

    if len(args.files) > 0:
        for fname in args.files:
            logging.info("Processing document {}".format(fname))
            with open(fname, "r", encoding="utf-8") as f:
                content = "".join(f.readlines())
                info = extract_abstract(content)
                print(info)
    else:
        content = "".join(sys.stdin.readlines())
        #content = re.sub(r"^%.*$","",content, re.MULTILINE)
        #print(content)
        info = extract_abstract(content)
        print(info)

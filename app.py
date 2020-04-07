#!./venv/bin/python

from functions import create_table,insert_table,view_table
import argparse
import sys

#Argparse Config
parser = argparse.ArgumentParser(description='TY Investments \
    Database Script')

parser.add_argument('-i', '--insert', help='Input data \
     into database', action='store_true')
parser.add_argument('-v', '--view', help='Show all data \
    inside money table', action='store_true')
args = parser.parse_args()

if __name__ == "__main__":
    print("running app.py")
    if args.insert:
        create_table()
        insert_table()
    elif args.view:
        view_table()
    else:
        pass
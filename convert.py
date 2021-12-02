#! /usr/bin/env python3
import csv
import sys

try:
    mailchimp_file = sys.argv[1]
except IndexError:
    print("Please provide the file to convert as an argument:")
    print("./convert.py mailchimp.csv")
    sys.exit(1)

try:
    with open(mailchimp_file) as import_csv, open("sendinblue.csv", "w") as export_csv:
        csvreader = csv.reader(import_csv)
        csvwriter = csv.writer(export_csv)

        header = next(csvreader)

        # Add the two new fields we need for the Sendinblue import
        header.append("SIB_OPT_IN")
        header.append("SIB_DOUBLE_OPT-IN")
        csvwriter.writerow(header)

        for row in csvreader:
            # Check OptIn field
            optin_time = row[13]
            if optin_time != "":
                row.append("Yes")
            else:
                row.append("")

            # Check Double OptIn field
            confirm_time = row[15]
            if confirm_time != "":
                row.append("1")
            else:
                row.append("2")

            csvwriter.writerow(row)


except FileNotFoundError:
    print("The provided filename does not exist")
    sys.exit(1)

#!/usr/bin/env python3
#
# Assignment: Mailroom, Part 2
# Chay Casso
# 2/11/2018

import collections

# Initial donor table with the donation values.
donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                    "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21], "Steve Ballmer": [5198.96, 654.98]}
answer = ""


def thank_you(thank_you_dict):
    full_name = ""
    while True:
        full_name = input("Please enter a full name. >")
        if full_name.lower() == "quit": return(thank_you_dict)
        if full_name.lower() == "list":
            print("Donor list:")
            print(list(thank_you_dict.keys()))
        else:
            donation_value_str = input("Please enter a donation amount. >")
            if donation_value_str.lower() == "quit": return(thank_you_dict)
            if full_name in thank_you_dict:
                thank_you_dict[full_name].append(donation_value_str)
            else:
                thank_you_dict[full_name] = donation_value_str
            print()
            print("\nDear {}:\n\n\tThank you for your generous donation of ${} to Save the Kids.\n\n-------------\n"
                  "Save the Kids\nsave@kids.org\n".format(full_name, donation_value_str))
            return(thank_you_dict)

def sum(input_table):
    result = 0
    for i in input_table:
        result = result + i
    return result

def create_report(create_report_dict):
    print("{:<20} | {:<10} | {:<10} | {:<10}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("----------------------------------------------------------------------------")

    ordered_create_report_dict = collections.OrderedDict(sorted(create_report_dict.items()))

    for key, table in ordered_create_report_dict:    
        print("{:<20}   ${:>10.2f}   {:>10d}   ${:>10.2f}".format(key, sum(table), len(table),
                                                             sum(table) / len(table)))


def send_letters(donor_table_dict):
    pass


# Main menu
if __name__ == "__main__":
    while True:
        print("1. Send a Thank You\n2. Create a Report\n3. Send Letters to All\n4. Quit")
        answer_dict = {"1": thank_you,
                       "2": create_report,
                       "3": send_letters,
                       "4": "quit"}
        answer = input("Please select an option. >")
        if answer == "4":
            print("Have a nice day.")
            break
        else:
            answer_dict[answer](donor_table_dict)
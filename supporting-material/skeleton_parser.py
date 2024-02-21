"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):

    items_table = open('items.txt', 'a')
    users_table = open('users.dat', 'a')
    bids_table = open('bids.dat', 'a')
    category_table = open('category.dat', 'a')
    bidders_table = open('bidders.dat', 'a')
    sellers_table = open('sellers.dat', 'a')

    user_exists = set()
    seller_exists = set()
    bidder_exists = set()

    print('hi')

    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """

            item_id = item["ItemID"]
            name = item["Name"].replace('"', '""')
            currently = transformDollar(item["Currently"])
            buy_price = transformDollar(item.get("Buy_Price", "NULL"))
            first_bid = transformDollar(item["First_Bid"])
            number_of_bids = item["Number_of_Bids"]
            start_date = transformDttm(item["Started"])
            end_date = transformDttm(item["Ends"])
            description = item["Description"].replace('"', '""')
            
            categories = item["Category"]
            
            for category in categories:
                category_table.write(f"{item_id}{columnSeparator}{category}\n")

            bids = item.get("Bids", [])
            for bid in bids:
                bidder = bid["Bid"]["Bidder"]
                bidder_id = bidder["UserID"]
                bidder_location = bidder["Location"]
                bidder_country = bidder["Country"]
                bidder_rating = bidder["Rating"]

                user = f"{bidder_id}{columnSeparator}{bidder_rating}{columnSeparator}{bidder_location}{columnSeparator}{bidder_country}\n"
                if user not in user_exists:
                    user_exists.add(user)
                    users_table.write(user)

                bidder = f"{bidder_id}\n"
                if bidder not in bidder_exists:
                    bidder_exists.add(bidder)
                    bidders_table.write(bidder)

                bidder_time = transformDttm(bidder["Time"])
                bidder_amount = transformDollar(bidder["Amount"])
                bids_table.write(f"{bidder_id}{columnSeparator}{bidder_time}{columnSeparator}{bidder_amount}\n")

            sellers = item.get("Seller", [])
            seller_location = item["Location"]
            seller_country = item["Country"]
            
            seller_id = sellers["UserID"]
            seller_rating = sellers["Rating"]

            items_table.write(f"""{item_id}{columnSeparator}{name}{columnSeparator}{currently}{columnSeparator}
                              {buy_price}{columnSeparator}{first_bid}{columnSeparator}{number_of_bids}{columnSeparator}
                              {start_date}{columnSeparator}{end_date}{columnSeparator}{description}{columnSeparator}{seller_id}\n""")

            user = f"{seller_id}{columnSeparator}{seller_rating}{columnSeparator}{seller_location}{columnSeparator}{seller_country}\n"
            if user not in user_exists:
                user_exists.add(user)
                users_table.write(user)

            seller = f"{seller_id}\n"
            if seller not in seller_exists:
                seller_exists.add(seller)
                sellers_table.write(seller)
            


            break    

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    print('hi')
    if len(argv) < 2:
        print ('Usage: python skeleton_json_parser.py <path to json files>', file=sys.stderr)
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        print(isJson(f))
        if isJson(f):
            parseJson(f)
            print ("Success parsing ", f)

if __name__ == '_main_':
    print('hi')
    main(sys.argv)
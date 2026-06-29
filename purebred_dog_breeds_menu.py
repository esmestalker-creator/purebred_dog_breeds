# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'purebred_dogs.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice = ""
while menu_choice != "-":
    menu_choice = input("This is a dog breeds database. \n" \
    "Read the information bellow, then type in the letter that corresponds to the infomation you want. \n\n" \
    "A) Raw data sorted alphabetically \n" \
    "B) Large dogs average size \n" \
    "C) Small dogs average size \n" \
    "D) Dogs without breathing issues \n" \
    "E) Shows how easy/difficult they are to look after \n" \
    "F) Lifespan of the dogs in the group 'Toy' \n" \
    "G) Price of Terriers and Hounds \n" \
    "H) The breeds of dogs with infomation about the registered amount in New Zealand \n" \
    "Type '-' if you would like to stop recieving infomation \n\n" \
    "Type Here: ").upper()

    if menu_choice == "A":
        print_query('raw_data_alphabetically')
    elif menu_choice == "B":
        print_query('large_dogs')
    elif menu_choice == "C":
        print_query('small_dogs')
    elif menu_choice == "D":
        print_query('no_breathing_issues')
    elif menu_choice == "E":
        print_query('easy_care')
    elif menu_choice == "F":
        print_query('lifespan_toy')
    elif menu_choice == "G":
        print_query('terrier_hound_price')
    elif menu_choice == "H":
        print_query('amount_nz_info')
    else:
        print('Please select from the following options')
"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: March 1, 2020
Final Project
Description: View my preferred stock list (selection is my own)
"""

import sys
import csv
from stock import Stock

# create an empty list to store the data from import
stocks = []


def get_stocks():
    """
    Open the csv file making sure the file can be opened
    """
    try:
        f = open('list.csv')
    except ValueError:
        print("Could not read {}".format('list.csv'))
        sys.exit()

    with f:
        reader = csv.reader(f)
        # loop through each row the csv file
        for row in reader:
            # create a dictionary
            stock_dict = {'name': row[0], 'tickler': row[1], 'price': row[2]}
            # create a stock object
            stock = Stock(stock_dict['name'], stock_dict['tickler'],
                          stock_dict['price'])
            # append the stock object to the list of stock
            stocks.append(stock)


def display_stock_info():
    """
    Display stock symbol and price
    """
    print("\nPrice listings as of 2-18-2020")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # loop through the stock list and display the price for each symbol
    for I in range(len(stocks)):
        print("{:30} | {:10} | {:10}".format(
                stocks[I].get_name(),
                stocks[I].get_tickler(),
                stocks[I].get_price()))
        print()


def initiate():
    """
    Prompts user response to interact with the data
    """
    reply = str(input('Please type y to view our listings or'
                      ' n to exit (case sensitive): ')).strip()
    try:
        # create a case sensitive prompt
        if reply == 'y':
            return True
        if reply == 'n':
            print('You have now exited our listing from 2-18-2020.')
            sys.exit()
        else:
            # capture any invalid inputs
            print('Invalid input, please enter y or n.')
            return initiate()
    except ValueError:
        return initiate()


def terminate():
    """
    Allows the user to terminate the program after it begins
    """
    user_input = input('Type e to end the view of our listings: ')
    # create a case sensitive prompt
    if user_input == "e":
        print('Thanks for viewing our listings. \nWe do not endorse'
              ' any of the following selections. \nConsult with a'
              ' financial advisor if you wish to invest.')
        sys.exit()
    else:
        # capture any invalid inputs
        print('Invalid input, please enter e to exit.')
        return terminate()


if __name__ == '__main__':
    """
    Recalls all the functions from the program
    """
    initiate()
    get_stocks()
    display_stock_info()
    terminate()

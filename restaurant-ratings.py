# your code goes here

import sys
file_name = sys.argv[1]


def put_restaurant_and_rating(restaurant_ratings):
    """Adds user inputted restaurant and rating
    """

    restaurant = raw_input("restaurant name: ")
    rating = raw_input("rating: ")
    restaurant_ratings[restaurant] = rating


def ratings_menu(restaurant_ratings):
    while True:
        print "Menu"
        print "1: See all ratings."
        print "2: Add a new restaurant and rating."
        print "3: Exit menu and print ratings."
        options = raw_input("Make a selection. \n")

        if options == "1":
            break
        elif options == "2":
            restaurant = raw_input("Please input a restaurant name: ")
            if restaurant == "3":
                break
            else:
                rating = raw_input("rating: ")
                restaurant_ratings[restaurant] = rating
        elif options == "3":
            break


def print_ratings(file_name):
    """Prints alphabetical restaurant names and their cooresponding ratings.
    """

    restaurant_ratings = {}
    for line in open(file_name):
        restaurant, rating = line.rstrip().split(":")
        restaurant_ratings[restaurant] = rating
    # print "before calling function", restaurant_ratings

    put_restaurant_and_rating(restaurant_ratings)

    # print "after calling previous function", restaurant_ratings

    for restaurant, rating in sorted(restaurant_ratings.iteritems()):
        print "{} is rated at {}.".format(restaurant, rating)


print_ratings(file_name)

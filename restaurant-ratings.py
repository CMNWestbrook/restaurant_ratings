# your code goes here

import sys
file_name = sys.argv[1]


def print_ratings(file_name):
    """Returns alphabetical restuarant names and their cooresponding ratings.
    """

    restaurant_ratings = {}
    for line in open(file_name):
        restaurant, rating = line.rstrip().split(":")
        restaurant_ratings[restaurant] = rating

    def get_restaurant_and_rating():
        restaurant = raw_input("restaurant name: ")
        rating = raw_input("rating: ")
        restaurant_ratings[restaurant] = rating

    get_restaurant_and_rating()

    for restaurant, rating in sorted(restaurant_ratings.iteritems()):
        print "{} is rated at {}.".format(restaurant, rating)


print_ratings(file_name)

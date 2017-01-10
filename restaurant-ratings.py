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

    for restaurant, rating in sorted(restaurant_ratings.iteritems()):
        print "{} is rated at {}.".format(restaurant, rating)

    print restaurant
    print line

print_ratings(file_name)

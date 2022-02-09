"""Restaurant rating lister."""


# put your code here



scores = open('scores.txt')

ratings_dict = {}

for line in scores:
    line = line.rstrip()
    words = line.split(':')
    ratings_dict[words[0]] = words[1]

new_restaurant = input("What restaurant do you want to rate? ")

new_rating = input("What rating (1-5) do you want to give this restaurant? ")

ratings_dict[new_restaurant] = new_rating

for restaurant, rating in sorted(ratings_dict.items()):
    print(f"{restaurant} is rated at {rating}.")
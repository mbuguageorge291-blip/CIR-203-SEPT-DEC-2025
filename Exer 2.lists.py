# Task 1: Create a list of 10 delivery routes
delivery_routes = [
    "Nairobi Central",
    "Mombasa Port",
    "Kisumu Lakeside",
    "Eldoret Express",
    "Nakuru Ridge",
    "Thika Highway",
    "Garissa Trail",
    "Nyeri Highlands",
    "Kitale Cargo",
    "Machakos Transit"
]

# Task 2: Append a new route and remove a discontinued one
delivery_routes.append("Lodwar Frontier")       # New route added
delivery_routes.remove("Garissa Trail")         # Discontinued route removed

# Task 3: Sort the list alphabetically and reverse it
delivery_routes.sort()
delivery_routes.reverse()

# Task 4: Count how many routes start with the letter “N”
count_N_routes = sum(route.startswith("N") for route in delivery_routes)

# Task 5: List comprehension for routes longer than 10 characters
long_routes = [route for route in delivery_routes if len(route) > 10]

# Output results
print("Updated Delivery Routes:", delivery_routes)
print("Number of routes starting with 'N':", count_N_routes)
print("Routes longer than 10 characters:", long_routes)

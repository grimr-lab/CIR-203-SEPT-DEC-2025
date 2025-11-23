routes = [
    "Nairobi-Mombasa",
    "Kisumu-Nairobi",
    "Nakuru-Eldoret",
    "Nairobi-Thika",
    "Mombasa-Malindi",
    "Naivasha-Nakuru",
    "Nairobi-Kisii",
    "Garissa-Nairobi",
    "Nyeri-Nairobi",
    "Nairobi-Machakos"
]
print("Original Routes:")
print(routes)
routes.append("Isiolo-Meru")
routes.remove("Nairobi-Thika")
print("\nAfter Adding and Removing Routes:")
print(routes)
routes.sort()
print("\nSorted Routes:")
print(routes)
routes.reverse()
print("\nReversed Routes:")
print(routes)
count_N = sum(1 for route in routes if route.startswith("N"))
print(f"\nNumber of routes starting with 'N': {count_N}")
long_routes = [route for route in routes if len(route) > 10]
print("\nRoutes longer than 10 characters:")
print(long_routes)

names_dict = {
    "John": {"age": 30, "city": "New York", "occupation": "Engineer"},
    "Sarah": {"age": {"key": 1000}, "city": "Los Angeles", "occupation": "Teacher"},
    "Michael": {"age": 35, "city": "Chicago", "occupation": "Doctor"},
    "Emily": {"age": 25, "city": "San Francisco", "occupation": "Artist"},
}

print(names_dict["John"])  # Calling a dictionary
print(
    names_dict["Sarah"]["age"]["key"]
)  # Calling a dictionary within a dictionary, in this case "Sarah"


# [{"One": 1}, []]

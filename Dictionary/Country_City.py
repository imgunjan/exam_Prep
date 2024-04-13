attribute = {
    "Nepal": {"City": "Kathmandu"},
    "Italy": {"City": "Rome"},
    "England": {"City": "London"},
}


for country, info in attribute.items():
    print(f"country: {country}, city:{info['City']}")

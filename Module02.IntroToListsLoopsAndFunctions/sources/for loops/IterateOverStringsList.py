#initialize a strings list
planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for planet in planets:
    if (planet == "Sun"):
        print(planet, "is a star.")
    else:
        print(planet, "is a planet.")
    
    if (planet == "Mercury"):
        print(planet, "is the closest planet to the Sun.")
    elif (planet == "Neptune"):
        print(planet, "is the farthest planet to the Sun.")

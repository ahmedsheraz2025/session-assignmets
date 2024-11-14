

def weight_on_planets(weight_on_earth,planet):
    all_planets = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 0.2360,
    "Saturn": 0.1081,
    "Uranus": 0.815,
    "Neptune": 0.1140
}
    if planet in all_planets:
        calculated = weight_on_earth* all_planets[planet]
        return f"Your weight on {planet} is {calculated}"
    else:
        return "Invalid planet name."
    
weight_on_earth = float(input("Enter your weight on Earth "))
planet = input("Enter a Planet ")
print(weight_on_planets(weight_on_earth,planet))
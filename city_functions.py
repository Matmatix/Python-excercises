def city_format (city, country, population=""):
    if population:
        output = city + ", " + country + " - " + population
    else:
        output = city + ", " + country
    return output.title()

def citiesName(city,country):
    return f' "{city}",{country}"'
first = citiesName("Nellore","India")
second = citiesName(country="India",city="Chennai")
thrid = citiesName("Kavali","India")
print(first)
print(second)
print(thrid)
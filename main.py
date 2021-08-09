from MainPackage import main_package_var
from MainPackage.SubPackage import sub_package_var

countries = main_package_var.countries
cities = main_package_var.cities
sbv = sub_package_var

flm = sub_package_var.flm

# print(countries)
# print(cities)
print(flm)
print()
print(sbv.add(2))
print()
print(sbv.test())

# for country in countries:
#     print(country, end = " ")

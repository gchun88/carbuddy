import requests,json;
base_url = 'https://vpic.nhtsa.dot.gov/api%s';
url_vehicles_makes= '/vehicles/GetAllMakes?format=json'
url_vehicles_makes='/vehicles/GetAllManufacturers?format=json'
url_vehicles_makes='/vehicles/GetManufacturerDetails/honda?format=xml'


url = base_url % url_vehicles_makes
r = requests.get(url);
print(r.text);

r

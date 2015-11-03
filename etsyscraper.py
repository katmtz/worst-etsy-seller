import requests
from taxonomy import *

class EtsyRequest:

    # Useful Constant Info
    api_key = "api_key=imc9efczkz0f1j2kq8gijv8p"
    base_url = "https://openapi.etsy.com/v2/"

    def getAllData(self):
	    taxonomy_dict = self.getTaxonomies()
	    sales = self.getSalesByCategory(taxonomy_dict)

    def getTaxonomies(self):
	    request = self.base_url + 'taxonomy/buyer/get/?' + self.api_key
	    json = requests.get(request).json()
	    categories = Categories(json)
	    print categories.data
	    return categories.data

    def getSalesByCategory(self, taxonomy_dict):
	    for category_id in taxonomy_dict:
		    self.searchByCategory(category_id)
	    return

    def searchByCategory(self, category_id):
        request = self.base_url + 'listings/active?taxonomy_id=' + str(category_id) + "&" + self.api_key
        response = requests.get(request)
        print response.json()

req = EtsyRequest()
req.getAllData()
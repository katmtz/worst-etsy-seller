"""
Taxonomy:
 - built from Etsy's Taxonomy json response


"""
class Taxonomy:
	tax_id = 0
	name = ""

	def __init__(self, name, id):
		self.tax_id = id
		self.name = name


class Categories:
	data = {}

	def __init__(self, json):
		results = json['results']
		for i in xrange(len(results)):
			taxonomy = Taxonomy(results[i]['name'], results[i]['category_id'])
			self.data[taxonomy.tax_id] = [taxonomy.name]
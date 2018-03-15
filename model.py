import csv
from app import db

"""
	Model
"""
class Catalog(db.Model):
	__tablename__ = 'data'
	id = db.Column(db.Integer, primary_key=True)
	hid = db.Column(db.String)
	content = db.Column(db.String)
	has_space = db.Column(db.Boolean)
	
	def __repr__(self):
		return "<hid = '%s'> %s\n" % (self.hid, self.content)

	def serialize(self):
		return {
			"hid": self.hid,
			"content": self.content,
			"has_space": self.has_space
		}
	
		
def add_catalog(data):
	"""
	Get the content string by hid.
	:param data:
	:type data: list
	:return:
	"""
	for item in data:
		catalog = Catalog(hid = item["hid"], content = item["content"], has_space = item["has_space"])
		db.session.add(catalog)
	
	
def load_csv(filename):
	"""
	:param filename:
	:return: [{"hid": str, "content": str, "has_space": bool}]
	"""
	res = []
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		
		for row in reader:
			item = {}
			item["hid"] = row[0]
			item["content"] = row[1]
			item["has_space"] = False if (row[2] == "0") else True
			res.append(item)
	return res
	
def query_by_hid(hid):
	"""
	
	:param hid:
	:return: dict
	"""
	query = db.session.query(Catalog)
	res = query.filter(Catalog.hid == hid).first()
	if res == None:
		return None
	else:
		return res.serialize()

def query_by_space(has_space):
	"""
	:param has_space:
	:return: list(dict)
	"""
	query = db.session.query(Catalog)
	res = query.filter(Catalog.has_space == has_space).all()
	if res == None:
		return None
	else:
		return [ele.serialize() for ele in res]

	
def start():
	# Command to generate 'ra_data_classifier_utf8.csv':
	#   bash $ iconv -f iso-8859-1 -t utf-8 < ra_data_classifier.csv > ra_data_classifier_utf8.csv
	add_catalog(load_csv("./data/ra_data_classifier_utf8.csv"))
	db.session.commit()

if __name__ == '__main__':
	start()

from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv


Base = declarative_base()
engine = create_engine('postgresql://localhost/test3')
# conn = engine.connect()
# conn.execution_options(isolation_level="AUTOCOMMIT")
# conn.execute('DROP DATABASE IF EXISTS test3;')
# conn.execute("CREATE DATABASE test3;")
# conn.execute("USE test3;")

Session = sessionmaker()
Session.configure(bind = engine)
session = Session()

"""
	Model
"""
class Catalog(Base):
	__tablename__ = 'data'
	id = Column(Integer, primary_key=True)
	hid = Column(String)
	content = Column(String)
	has_space = Column(Boolean)
	
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
		# print catalog
		session.add(catalog)
	
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
	query = session.query(Catalog)
	res = query.filter(Catalog.hid == hid).first()
	if res == None:
		return None
	else:
		return res.serialize()
		
	
def main():
	Base.metadata.create_all(engine)
	# bash $ iconv -f iso-8859-1 -t utf-8 < ra_data_classifier.csv > ra_data_classifier_utf8.csv
	add_catalog(load_csv("./ra_data_classifier_utf8.csv"))
	session.commit()


main()
	

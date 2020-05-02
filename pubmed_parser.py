import xml.etree.ElementTree as ET


tree = ET.parse('pubmed_result.xml')
articles = list(tree.iter("Article"))


def parse_abstract(article):
	abstract = article.findall('Abstract')
	if len(abstract) > 0:
		result = "\n".join([item.text for item in abstract[0].getchildren()])
	else:
		result = None
	return result



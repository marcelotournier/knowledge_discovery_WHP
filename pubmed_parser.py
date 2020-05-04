"""
The pubmed_parser helper module

Author: Marcelo Tournier

Objective: Helper classes to parse data from pubmed xml files.
"""
import xml.etree.ElementTree as ET
from pandas import DataFrame


def parse_articles(xmlfile='pubmed_result.xml'):
    """
    Parses a xml pubmed file into Article objects.
    Inputs:
        - xmlfile (str): path+xml filename
    Output: A list with "Article xml objects"

    Example:
        articles = parse_articles()
    """
    tree = ET.parse(xmlfile)
    return list(tree.iter("Article"))


def parse_abstract(article):
    """
    Parses the Abstract object from Article object, as string.
    Inputs:
        - xml Article object
    Output: A string with the Abstract object, or None if no Abstract is found.

    Example:
        articles = parse_articles("pubmed_result.xml")
        parse_abstract(articles[0])
    """
    abstract = article.findall('Abstract')
    if len(abstract) > 0:
        result = "\n".join([item.text for item in abstract[0].getchildren()])
    else:
        result = None
    return result


def parse_title(article):
    """
    Parses the Title object from Article object, as string.
    Inputs:
        - xml Article object
    Output: A string with the Title object, or None if no Abstract is found.

    Example:
        articles = parse_articles("pubmed_result.xml")
        parse_title(articles[0])
    """
    title = article.findall('ArticleTitle')
    if len(title) > 0:
        result = title[0].text
    else:
        result = None
    return result


def get_dataframe(xmlfile='pubmed_result.xml'):
    """
    Parses the Title and Abstract objects from a pubmed xml file,
    as a Pandas Dataframe.

    Inputs:
        - xmlfile (str): path+xml filename
    Output: A pandas dataframe with the title and abstracts.
    NaN will be imputed if no value is found in the Article object.

    Example:
        data = get_dataframe('pubmed_result.xml')
    """
    articles = parse_articles(xmlfile)
    items = [(parse_title(item), parse_abstract(item)) for item in articles]
    return DataFrame(items, columns=["title", "abstract"])

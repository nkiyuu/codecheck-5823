#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import urllib.request
import chardet

def get_numFound(keyword):
	_quote = urllib.parse.quote_plus(keyword)
	response = urllib.request.urlopen("http://54.92.123.84/search?q=Keyword:" + _quote + "&ackey=" + ACCESS_KEY)
	tree = ET.parse(response)
	root = tree.getroot()
	return int(root.find(".//result").attrib['numFound'])

def main(argv):
	inputs = input()
	keywords = inputs.split(",")
	ACCESS_KEY = "869388c0968ae503614699f99e09d960f9ad3e12"
	keyword_numFound_dict = {}
	for keyword in keywords:
		keyword_numFound_dict[keyword] = get_numFound(keyword)

	answer_tupple = max([(v,k) for k,v in keyword_numFound_dict.items()])
	print("{name: %s, count: %s}" % (answer_tupple[1], answer_tupple[0]))
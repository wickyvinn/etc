from bs4 import BeautifulSoup
import requests

def getRating(soup):
	biz_Rating = soup.find("div", {"id": "bizRating"})
	rating_object = biz_Rating.find('div', attrs={'class': 'rating'})
	get_i_attrs = rating_object.find('i')
	rating_final = get_i_attrs.attrs['title']
	return rating_final

def getDollaSigns(soup):
	price_tip = soup.find("span", {"id": "price_tip"})
	return price_tip.get_text()

def getCategory(soup):
	category_object = soup.find("p", {"id": "bizCategories"})
	display_object = category_object.find("span",{"id":"cat_display"})
	a_object = display_object.a.get_text()
	return str(a_object).strip()

business_names = [

	"mamas-san-francisco",
	"farmerbrown-san-francisco",
	'rosamunde-sausage-grill-san-francisco',
	'tacolicious-san-francisco'

]

def run_scraper():
	for business_name in business_names:
		r = requests.get('http://www.yelp.com/biz/'+business_name+'?ob=1',allow_redirects=True)
		soup = BeautifulSoup(r.text)
		print business_name
		print "Category:",getCategory(soup)
		print "Rating:",getRating(soup)
		print "Dollar Signs:",getDollaSigns(soup)
		print "# of Dollar Signs:",len(getDollaSigns(soup))
		print "\n"

run_scraper()

from bs4 import BeautifulSoup
import requests

def getRating(business_name): # as stated exactly

	r = requests.get('http://www.yelp.com/biz/'+business_name+'?ob=1',allow_redirects=True)
	soup = BeautifulSoup(r.text)
	biz_Rating = soup.find("div", {"id": "bizRating"})
	rating_object = biz_Rating.find('div', attrs={'class': 'rating'})
	get_i_attrs = rating_object.find('i')
	rating_final = get_i_attrs.attrs['title']
	return rating_final

business_names = [

	"mamas-san-francisco",
	"farmerbrown-san-francisco",
	'rosamunde-sausage-grill-san-francisco',
	'tacolicious-san-francisco'

]

for business_name in business_names:
	print business_name,"has a",getRating(business_name)
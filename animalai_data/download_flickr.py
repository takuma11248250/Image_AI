from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報

key = "1f908264d42ed2920221353b4c847984"
secret = "70985a5305a8400f"
wait_time = 1

#　保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
	text = animalname,
	par_page = 400,
	media = 'photos',
	sort = 'relevance',
	sate_search = 1,
	extras = 'url_q, license'
)

photos = result['photos']
for i, photo in enumerate(photos['photo']):
	url_q = photo['url_q']
	fliepath = savedir + '/' + photo['id'] + '.jpg'
	if os.path.exists(fliepath): continue
	urlretrieve(url_q, fliepath)
	time.sleep(wait_time)
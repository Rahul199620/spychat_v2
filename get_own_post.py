import requests
#import json
import urllib
from constants import APP_ACCESS_TOKEN , BASE_URL
def get_own_post():
    #function logic
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
  #  print json.dumps(own_media, indent=4)
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
           # video_new = own_media['data'][0]['id'] + '.mp4'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            video_url = own_media ['data'] [0] ['videos']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
         #   urllib.urlretrieve(video_url, video_new)
            print 'Your image has been downloaded!'
         #   print 'your video has been downloaded'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

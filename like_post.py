import requests
from constants import APP_ACCESS_TOKEN, BASE_URL
from getpost_id import get_post_id

def like_post(insta_username):
    media_id = get_post_id(insta_username)
    like_post_url= (BASE_URL + "media/%s/likes" ) % (media_id)
    payload = {'access_token': APP_ACCESS_TOKEN}
    print "Post request url %s " %(like_post_url)
    like = requests.post(like_post_url,payload).json()
    if like['meta']['code']== 200:
        print ('liked successfully')
    else:
        print ('your like was unsuccess full')
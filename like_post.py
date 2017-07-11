import requests
from constants import APP_ACCESS_TOKEN, BASE_URL

def like_post(insta_username, option, post_selection, n):
    media_id = search_post_by_choice(insta_username, option, post_selection, n)
    like_post_url= BASE_URL + "media/" + media_id + "/likes"
    payload = {'access_token': APP_ACCESS_TOKEN}
    like = requests.post(like_post_url,payload).json()
    if like['meta']['code']== 200:
        print ('liked successfully')
    else:
        print ('your like was unsuccess full')
import requests
from constants import APP_ACCESS_TOKEN, BASE_URL
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == none:
        print 'user doesnot exist'
        exit()
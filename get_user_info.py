#fteches user info from instagram
from get_user_id import get_user_id
from constants import APP_ACCESS_TOKEN, BASE_URL
import requests
def get_user_info(insta_username):
    #function logic
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'username: %s' % (user_info['data']['username'])
            print 'no of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'no of people following you %s' % (user_info['data']['counts']['follows'])
            print 'no of posts %s' % (user_info['data']['counts']['media'])
        else:
            print 'user does not exist'

    else:
        print 'status code other than 200 revieved'

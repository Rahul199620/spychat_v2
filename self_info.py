#self info function
import requests
from constants import APP_ACCESS_TOKEN, BASE_URL
def self_info():
    #function logic
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
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




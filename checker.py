import urllib.request
import bs4
import json

g_github_username = 'polcats'

def fetchUsers(mode):
    page = 1
    has_more = True
    users = []
    url = 'https://api.github.com/users/' + g_github_username + '/' + mode + '?per_page=100'

    while has_more:
        fetched_users = json.loads(urllib.request.urlopen(url + '&page=' + str(page)).read())
        if len(fetched_users) == 0:
            has_more = False
        else:
            users.extend(fetched_users)
            page += 1
    return users

def getUserNames(data):
    if len(data) == 0:
        return []
    else:
        usernames = []
        for item in data:
            usernames.append(item['login'])
        return usernames

g_followers = getUserNames(fetchUsers('followers'))
g_following = getUserNames(fetchUsers('following'))

def notFollowingBack():
    return set(g_following) - set(g_followers)

def needToFollowBack():
    return set(g_followers) - set(g_following)






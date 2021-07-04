# Imports

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np

# set global constants
HEADER = {
        'user-agent': 
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Cache-Control':'no-cache'
}

COLUMNS  =  [ 'Name', 'Nickname', 'City', 'Work', 
             'Followers', 'Following', 'Likes', 
             'Repos', 'Contributions' ]


# first we need to get all users

def get_users(user, what):
    """
    Return all followers of a given user.

    @type user: string
    @param user: a github alias

    @type what: string
    @param what: could be 'followers' or 'following'

    @rtype: list
    @return: a list of users
    """
    
    url = 'https://github.com/{}?page={}&tab={}'
    results = []
    i = 0
    while True:
        # page number
        i+=1
        # link to the html of a given page number
        link = url.format(user, i, what)
        html = requests.get(link, headers=HEADER, timeout=10).text
        
        # Since there are 50 users per page
        # we need to make sure that we got them all
        if('You’ve reached the end of' in html):
            # we reached an empty page
            break
            
        soup = bs(html, 'lxml')
        nicknames = soup.find_all('span', class_='Link--secondary')
        for nickname in nicknames:
            results.append(nickname.text)
        
    return results


def extract_info(user):
    """
    Return a list of information about user.

    @type user: string
    @param user: a github alias

    @rtype: list
    @return: [full_name, user, city, work, followers, following, likes, repos, contributions]
    """

    # create bs object
    user_gh = 'https://github.com/{}'.format(user)
    html = requests.get(user_gh, headers=HEADER, timeout=10)
    soup = bs(html.text, 'lxml')
    
    # extract info
    try :
        full_name = soup.find('span', attrs={'itemprop':'name'}).text.strip()
    except:
        full_name = np.NAN
    
    try:
        city = soup.find('span', class_='p-label').text.strip()
    except:
        city = np.NAN
    try:
        work = soup.find('span', class_='p-org').text.strip()
    except:
        work = np.NAN

    try:
        repos = soup.find('span', class_='Counter').text.strip()
    except:
        repos = np.NAN
    try:
        contributions = soup.find('h2', class_='f4 text-normal mb-2').text.split()[0]
    except:
        contributions = np.NAN
        
    numbers = soup.find_all('span', class_='text-bold color-text-primary')
    try:
        followers = numbers[0].text
    except:
        followers = np.NAN
    
    try:
        following = numbers[1].text
    except:
        following = np.NAN
    
    try:
        likes = numbers[2].text
    except:
        likes = np.NAN
        
        
    return [full_name, user, city, work, followers, following, likes, repos, contributions]
    


def  github_crawler (user, what, fname='github_users_info'): 
    """
    main function

    @type user: string
    @param user: a github alias

    @type what: string
    @param what: could be 'followers' or 'following'

    @type fname: string
    @param fname: name of the csv file

    @rtype: csv file
    @return: fname csv file      
    """ 
    results = []
     
    users  =  get_users(user, what) 
    print("Crawling user's github. That can take some time. Please wait a moment!")
    for gh_user in users:
        result = extract_info(gh_user)
        results.append(result)
        print('.', flush=True, end='')
    
    
    df = pd.DataFrame(results, columns=COLUMNS)
    
    df.to_csv(fname + '.csv')
    print(f'\nFile saved under "{fname}.csv"')


if __name__ == "__main__":
    user = 'skacem'

    what = ['followers', 'following']

    github_crawler(user, what[1])
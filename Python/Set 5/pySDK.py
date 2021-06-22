import requests

def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code != 200:
        raise ApiError('Cannot fetch all tasks: {}'.format(response.status_code))
    for post_item in response.json():
        print('{}.\nTITLE: {}\nBODY: {}'.format(post_item['id'], post_item['title'], post_item['body']))

def get_user_posts(userId):
    response = requests.get('https://jsonplaceholder.typicode.com/posts?userId={}'.format(userId))
    if response.json() == []:
        print('Error: No such post found')
    for post_item in response.json():
        print('{}.\nTITLE: {}\nBODY: {}'.format(post_item['id'], post_item['title'], post_item['body']))

def get_posts_details(title):
    response = requests.get('https://jsonplaceholder.typicode.com/posts?title={}'.format(title))
    if response.json() == []:
        print('Error: No such post found')
    for post_item in response.json():
        print('UserId: {}\nId: {}\nTitle: {}\nBody: {}'.format(post_item['userId'], post_item['id'], post_item['title'], post_item['body']))

def get_comments():
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    if response.status_code != 200:
        raise ApiError('Cannot fetch all tasks: {}'.format(response.status_code))
    for post_item in response.json():
        print('{}.\n{}\n{}\n{}'.format(post_item['id'], post_item['name'], post_item['email'], post_item['body']))

def get_post_comments(postId):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/{}/comments'.format(postId))
    if response.json() == []:
        print('Error: No such post found')
    for comment_item in response.json():
        print('{}.\nNAME: {}\nEMAIL: {}\nBODY: {}'.format(comment_item['id'], comment_item['name'], comment_item['email'], comment_item['body']))
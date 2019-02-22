#this module uses hacker new api to get some info and store it in a json file

import requests
import json

from operator import itemgetter

# Make an API call and store the responseself.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Process info about each submission
submission_ids = r.json()
print(f'No. of submission ids: {len(submission_ids)}')
submission_dicts = []
for submission_id in submission_ids:
    # Make a seperate API call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{str(submission_id)}.json'
    submission_r = requests.get(url)
    print(f'Submission status code: {submission_r.status_code}')
    response_dict = submission_r.json()

    # build submission dictionary for each submission.
    # Not sure if a key exist in a dict use dict.get(key, False)
    submission_dict = {
                'title': response_dict['title'],
                'link': f'http://news.ycombinator.com/item?id={str(submission_id)}',
                'comments': response_dict.get('descendants', 0)
            }
    # add dictionary to the list of dictionaries
    submission_dicts.append(submission_dict)

# sort list
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

# for submission_dict in submission_dicts:
#     print(f'\nTitle: {submission_dicts["title"]}')
#     print(f'Discussion link: {submission_dicts["link"]}')
#     print(f'Comments: {submission_dicts["comments"]}')

filename = 'submission-dicts.json'
with open(filename, 'a') as f:
    json.dump(submission_dicts, f)

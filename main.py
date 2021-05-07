import requests
import json


def get_tweets_by_word(word, bearer_token):
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    param = {'q': word, 'count': 100, 'result_type': 'recent'}
    header = {'Authorization': f'Bearer {bearer_token}'}
    response = requests.get(url, headers=header, params=param)
    print(response.json())
    return response.json()


def save_json_to_file(file_name, file_path, data):
    with open(file_path + file_name, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    bearer_token = input('please enter your twitter bearer token:\n')
    word_to_find = input('Please enter a word to search for in tweets:\n')

    json_data = get_tweets_by_word(word=word_to_find, bearer_token=bearer_token)
    save_json_to_file(file_path='twitter_responses/', file_name=f'{word_to_find}.json', data=json_data)

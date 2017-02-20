import requests
import re
import json

def spellchecker(q):
    url = "https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn"
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    params = {
        '_callback': 'window.mycallback',
        'q':q,
        }

    response = requests.get(url, params=params, headers=headers).text
    response = response.replace(params['_callback'] + '(','')
    response = response.replace(');','')
    response_dict = json.loads(response)
    result_text = response_dict['message']['result']['html']
    result_text = re.sub(r'<\/?.*?>', '', result_text)
    return result_text

if __name__ == '__main__':
    line = input('')
    print(spellchecker(line))

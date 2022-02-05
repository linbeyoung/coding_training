from os import read
import re
import json
import os
import threading
import time
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def read_html(path):
    with open(path, 'r') as hf:
        hf_content = hf.read()
    patt = re.compile(r'https://leetcode-cn.com/problems/(.*?)"')
    res_list = patt.findall(hf_content)
    for i in res_list[:3]:
        print('https://leetcode-cn.com/problems/' + i)
        url = 'https://leetcode-cn.com/problems/' + i
        get_proble_content(url, i)
    # print(res_list)
    return res_list
    
def get_proble_content(problemUrl,title):
    response = requests.get(problemUrl)
    print(response)
    setCookie = response.headers["Set-Cookie"]
    '''
    print(setCookie)
    setCookie = json.loads(setCookie)
    print(type(setCookie))
    '''
    # try:
    pattern = re.compile("csrftoken=(.*?);.*?",re.S)
    print(pattern, setCookie)
    csrftoken = re.search(pattern, setCookie)
    print(csrftoken)
    url = "https://leetcode.com/graphql"
    data = {"operationName":"getQuestionDetail",
            "variables":{"titleSlug":title},
            "query":"query getQuestionDetail($titleSlug: String!) {\n  isCurrentUserAuthenticated\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    translatedTitle\n    questionTitleSlug\n    content\n    translatedContent\n    difficulty\n    stats\n    allowDiscuss\n    contributors\n    similarQuestions\n    mysqlSchemas\n    randomQuestionUrl\n    sessionId\n    categoryTitle\n    submitUrl\n    interpretUrl\n    codeDefinition\n    sampleTestCase\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    judgerAvailable\n    infoVerified\n    envInfo\n    urlManager\n    article\n    questionDetailUrl\n    libraryUrl\n    companyTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    __typename\n  }\n  interviewed {\n    interviewedUrl\n    companies {\n      id\n      name\n      slug\n      __typename\n    }\n    timeOptions {\n      id\n      name\n      __typename\n    }\n    stageOptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  subscribeUrl\n  isPremium\n  loginUrl\n}\n"
            }
    headers = {
        'x-csrftoken': csrftoken.group(1),
        'referer':problemUrl,
        'content-type':'application/json',
        'origin':'https://leetcode.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
    cookies = {'__cfduid':'d9ce37537c705e759f6bea15fffc9c58b1525271602',
                '_ga':'GA1.2.5783653.1525271604',
                '_gid':'GA1.2.344320119.1533189808',
                'csrftoken':csrftoken.group(1),
                ' _gat':'1'}
    #payload表单为json格式
    
    dumpJsonData = json.dumps(data)
    response = requests.post(url,data = dumpJsonData, headers = headers,cookies = cookies)
    dictInfo = json.loads(response.text)
    content = dictInfo["data"]["question"]["content"]
    print(content)
    soup = BeautifulSoup(content, 'lxml')
    save_problem(title,soup.prettify())
    # except Exception as e:
    #     print(e)
    #     print("错误："+ problemUrl)

    
if __name__ == '__main__':
    # main()
    path_list = [
        'problems/算法训练营2021版-本周作业.html',
    ]
    for path in path_list:
        read_html(path)
    pass
    
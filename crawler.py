# 用于爬取维基百科中的数据 例如 英文字母出现频率
import json
import requests
from bs4 import BeautifulSoup


# 将字符串“10.8%”转化为float数据类型的“10.8”
def percentage_to_float(percentage):
    return float(percentage.strip('%'))


def get_letter_frequency():
    url = 'https://en.wikipedia.org/wiki/Letter_frequency'
    response = requests.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='wikitable sortable floatright')
    tbody = table.find('tbody')
    items = tbody.find_all('tr')[2:28]

    result = {}

    for item in items:
        tds = item.find_all('td')[0:2]
        result[tds[0].text.strip().lower()] = percentage_to_float(tds[1].text.strip())
    assert len(result) == 26

    # result 降序排列
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    return result


# 爬取bigram数据，即双字符出现频率
def get_bigram_frequency():
    url = 'https://en.wikipedia.org/wiki/Bigram'
    response = requests.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', class_='mw-content-ltr mw-parser-output')
    pre = div.find('pre').text
    # 提取pre中数据
    pre = pre.strip().replace('       ', ' ').replace('\n', ' ').split(' ')
    result = {}
    for i in range(0, len(pre), 2):
        result[pre[i]] = percentage_to_float(pre[i + 1])
    # result 降序排列
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    return result


# 爬取trigram数据，即三字符出现频率
def get_trigram_frequency():
    url = 'https://en.wikipedia.org/wiki/Trigram'
    response = requests.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='wikitable sortable')
    tbody = table.find('tbody')
    items = tbody.find_all('tr')[1:]

    result = {}

    for item in items:
        tds = item.find_all('td')[1:]
        if "%" not in tds[1].text:
            continue
        result[tds[0].text.strip()] = percentage_to_float(tds[1].text.strip())

    # result 降序排列
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    return result


if __name__ == '__main__':
    result = get_letter_frequency()
    results = {'char': result}
    result = get_bigram_frequency()
    results['bigram'] = result
    result = get_trigram_frequency()
    results['trigram'] = result

    # 将result保存为json格式
    with open('letter_frequency.json', 'w') as f:
        json.dump(results, f)
    print('爬取完成')

    # 从json中读取数据
    with open('letter_frequency.json', 'r') as f:
        data = json.load(f)
    print(f'char: {data["char"]}')
    print(f'bigram: {data["bigram"]}')
    print(f"trigram: {data['trigram']}")

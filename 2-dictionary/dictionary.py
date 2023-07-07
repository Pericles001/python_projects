import json


def get_line():
    try:
        #I want to print first line of json file
        data = [json.loads(line)
                for line in open('data.json', 'r', encoding='utf-8')]
        print(data[0])
    except Exception as e:
        print(e)


get_line()
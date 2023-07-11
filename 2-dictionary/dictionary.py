import json


def save_line():
    """
    Method to save each line of dictionary in a file
    :return:
    """
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            first_line = file.readline()
            data = json.loads(first_line)
            # store datas in a file and replace ',' with '\n'
            with open('data.txt', 'w', encoding='utf-8') as file:
                for key, value in data.items():
                    line = f"{key}: {value}\n"
                    file.write(line)
    except FileNotFoundError:
        print("File 'data.json' not found.")
    except json.JSONDecodeError:
        print("Unable to decode the JSON data in the first line.")
    except Exception as e:
        print("An error occurred:", e)


def take_argument(target_word):
    """
    this function will take a word as argument

    :return:
    """
    try:
        print("Enter a word: \m")
        target_word = input()
        return target_word
    except Exception as e:
        print(e)

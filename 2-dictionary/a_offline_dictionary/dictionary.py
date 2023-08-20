import json
import os


def save_line():
    """
    Method to save each line of dictionary in a file
    :return:
    """
    try:
        script_directory = os.path.dirname(__file__)
        data_json_path = os.path.join(script_directory, 'data.json')

        with open(data_json_path, 'r', encoding='utf-8') as file:
            first_line = file.readline()
            data = json.loads(first_line)
            # store datas in a file and replace ',' with '\n'
            with open('data.txt', 'w', encoding='utf-8') as file_2:
                for key, value in data.items():
                    line = f"{key}: {value}\n"
                    file_2.write(line)
    except FileNotFoundError:
        print("File 'data.json' not found.")
    except json.JSONDecodeError:
        print("Unable to decode the JSON data in the first line.")
    except Exception as e:
        print("An error occurred:", e)


def redirect_to_offline():
    """
    Method to redirect to offline dictionary
    :return:
    """
    try:
        save_line()
        while True:
            offline_target = take_argument("Welcome to offline dictionary.")
            print(search_word_offline(offline_target))
            if offline_target == "00":
                break
    except Exception as e:
        print(e)


def take_argument(msg_text=""):
    """
    this function will take a word as an argument

    :return:
    """
    try:
        print(msg_text)
        print("Enter a word to get their meaning or enter 00 to exit: \n")
        target_word = input()
        return target_word.lower()
    except Exception as e:
        print(e)


def search_word_offline(target):
    """
    Method to search a word in the dictionary using target and data.txt file
    :param target:
    :return:
    """
    try:
        with open('data.txt', 'r', encoding='utf-8') as file:
            # the word is the sequence before ':' so we split the line and compare the first element
            for line in file:
                if line.split(':')[0] == target:
                    return line
                elif target == "00":
                    return "Goodbye!"
            return "The word doesn't exist. Please double check it."
    except Exception as e:
        print("Error:" + str(e))

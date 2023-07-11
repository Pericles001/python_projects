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


def take_argument(target_word=""):
    """
    this function will take a word as argument

    :return:
    """
    try:
        print("Welcome to our custom dictionary.")
        print("Enter a word to get their meaning or enter 00 to exit: \n")
        target_word = input()
        return target_word.lower()
    except Exception as e:
        print(e)


def search_word(target):
    """
    Method to search a word in the dictionary using target and data.txt file
    :param target:
    :return:
    """
    with open('data.txt', 'r', encoding='utf-8') as file:
        # the word is the sequence before ':' so we split the line and compare the first element
        for line in file:
            if line.split(':')[0] == target:
                return line
            elif target == "00":
                return "Goodbye!"
        return "The word doesn't exist. Please double check it."

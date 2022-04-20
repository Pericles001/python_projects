# tHIS IS THE MAIN FILE PROGRAM TO SHUFFLE ITEMS
from random import shuffle

items = []

def get_items():
    """ Get items to shuffle as   a list"""
    print('Enter items to shuffle, one per line.\n')
    print("Enter 'done' when finished.\n")
    item = input("Item: ")
    if item == "done":
        return items
    while item != "done":
        items.append(item)
        item = input("Item: ")
    return items


def shuffle_items():
    """Shuffle items which where taken"""
    print("Shuffling items...")
    shuffle(items)
    return items[1]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_items()
    print (items[1])
    shuffle_items()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

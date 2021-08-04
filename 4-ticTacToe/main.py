# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


board = [' ' for x in range(10)]


def game():
    def insertLetter(letter, pos):
        board[pos] = letter

    def printBoard(board):
        print('  |    |  ')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('  |    |  ')
        print('----------')
        print('  |    |  ')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('  |    |  ')
        print('----------')
        print('  |    |  ')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('  |    |  ')
        print('----------')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


board = [' ' for x in range(10)]


def game():
    def insertLetter(letter, pos):
        board[pos] = letter

    def spaceIsFree(pos):
        return board[pos] == ''

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

    def isBoardFull(board):
        if board.count(' ') > 1:
            return False
        else:
            return True

    def isWinner(b, l):
        return (b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (
                b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[5] == l and b[9] == l) or (
                       b[3] == l and b[5] == l and b[7] == l) or (b[1] == l and b[4] == l and b[7] == l) or (
                       b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l)

    def plzyerMove():
        run = True
        while run:
            move = input("Please, select a position to enter the X between 1 to 9")
            try:
                move = int(move)
                if move > 0 and move < 10:
                    if spaceIsFree(move):
                        run = False
                        insertLetter('X', move)
                    else:
                        print('Sorry, this space is occupied')
                else:
                    print('Please, type a number between 1 and 9')

            except:
                print('Please, type a number')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

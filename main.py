import chker


def game():
    # Prompt user for board size

        while True:
            board_size = int(input("Enter board size (between 4 and 16): "))
            if 4 <= board_size <= 16:
                break
            print("Invalid board size. Please enter a number between 4 and 16.")

    # Generate board
        print('\nChecker Board')
        board = chker.build_board(board_size)
        # pivoted_board = chker.pivot_board(board)
    # Print board
        print(board)
        print('\nPivoted Board')
        print("*"*10)
        chker.pivot_board(board)
    # Count items on board
        empty_count = chker.get_count(board, "Empty")
        red_count = chker.get_count(board, "Red")
        black_count = chker.get_count(board, "Black")
        # pivoted_board = chker.pivot_board(board)

    # Print counts
        print(f"\nEmpty cells: {empty_count}")
        print(f"Red checkers: {red_count}")
        print(f"Black checkers: {black_count}")

        # print(f"Black checkers: {pivoted_board}")

if __name__ == "__main__":
   game()
while True:
    print('Do you want to resize the board(y/n)')
    choice = input()
    if choice == 'y':
        game()
    elif choice == 'n':
        break
    else:
        print('Please enter valid choice y or n')
        continue

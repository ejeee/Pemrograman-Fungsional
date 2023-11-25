import random

def create_board(height, width, default_char='-'):
    # Membuat board dengan list comprehension
    board = [[default_char for _ in range(width)] for _ in range(height)] #list 2d presentasi board
    return board

generate_random_position = lambda height, width: (random.randint(0, height - 1), random.randint(0, width - 1))

def place_piece(board, row, col, piece_char):
    # Menempatkan bidak pada posisi yang ditentukan
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        board[row][col] = piece_char
    else:
        print("Posisi di luar batas board.")

def print_board(board):
    for row in board:
        print(' '.join(row))

def move_piece(board, position, move_direction):
    # Fungsi ini akan memindahkan bidak ke arah yang ditentukan
    row, col = position
    new_row, new_col = row, col

    if move_direction == 'w' and row > 0 and board[row - 1][col] != '#':
        new_row = row - 1
    elif move_direction == 's' and row < len(board) - 1 and board[row + 1][col] != '#':
        new_row = row + 1
    elif move_direction == 'a' and col > 0 and board[row][col - 1] != '#':
        new_col = col - 1
    elif move_direction == 'd' and col < len(board[0]) - 1 and board[row][col + 1] != '#':
        new_col = col + 1

    if (new_row, new_col) != (row, col):
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
        return new_row, new_col
    else:
        return row, col

def main():

    print("~~~ Selamat datang dalam permainan! ~~~")
    print("----------------------------------------------------------------------")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O) gunakan keyboard WASD untuk berjalan")
    print("----------------------------------------------------------------------")
    print(" ")

    height = int(input("Masukkan panjang board: "))
    width = int(input("Masukkan lebar board: "))

    board = create_board(height, width)

    # Membuat generator posisi awal bidak dan tujuan bidak secara acak
    position_generator = lambda: generate_random_position(height, width)
    start_row, start_col = position_generator() #awal
    goal_row, goal_col = position_generator() #tujuan

    place_piece(board, start_row, start_col, 'A')
    place_piece(board, goal_row, goal_col, 'O')

    print(" ")
    print("Let's play... This is your game board")
    print_board(board)

    repeat = input(
        "New Position (Y/N)?"
    ).lower()

    ulang = 0

    while repeat == "y":
     if (board[start_row][start_col] == board[goal_row][goal_col]):
        print("Index A dan O Sama")
        print("Generating Ulang ...")
     else:
        board[start_row][start_col] = "-"
        board[goal_row][goal_col] = "-"

        # exception handling
        try:
            positions = position_generator()
            start_row, goal_row = positions[0], positions[1]
            board[start_row][start_col] = "A"
            board[goal_row][goal_col] = "O"
        except IndexError:
            print("Kesalahan dalam menghasilkan posisi awal dan tujuan.")

        print_board(board)
        repeat = input(
            "New Position (Y/N)?"
        ).lower()
        ulang += 1
        if ulang == 3:
            print("Maksimal 3 kali dalam mengubah posisi!")
            repeat = "n"

    max_moves = height + width

    move_count = 0

    while move_count < max_moves:
        move = input("Masukkan arah pergerakan (W/A/S/D) atau 'q' untuk keluar: ").lower()

        if move == 'q':
            print("Anda keluar dari permainan.")
            break

        if move not in ['w', 'a', 's', 'd']:
            print("Masukkan arah yang benar!")
            continue

        start_row, start_col = move_piece(board, (start_row, start_col), move)
        move_count += 1
        print_board(board)

        if (start_row, start_col) == (goal_row, goal_col):
            print("Selamat! Anda menang!")
            break

    # Jika pemain melampaui jumlah maksimum langkah, mereka kalah.
    if move_count >= max_moves and (start_row, start_col) != (goal_row, goal_col):
        print("Anda kalah karena tidak mencapai tujuan dalam jumlah langkah maksimum!")


if __name__ == "__main__":
    main()
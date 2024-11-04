def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i+1]} {cells[i+2]} |")
    print("---------")


def check_state(cells):
    lines = [cells[0:3], cells[3:6], cells[6:9], 
             cells[0:9:3], cells[1:9:3], cells[2:9:3],
             cells[0:9:4], cells[2:7:2]]
    
    if "XXX" in lines:
        return "X wins"
    if "OOO" in lines:
        return "O wins"
    if "_" not in cells:
        return "Draw"
    return "Game not finished"


def is_valid_move(cells, x, y):
    if not (1 <= x <= 3 and 1 <= y <= 3):
        return "Coordinates should be from 1 to 3!"
    index = (x - 1) + (y - 1) * 3
    if cells[index] != "_":
        return "This cell is occupied! Choose another one!"
    return None


def make_move(cells, x, y, player):
    index = (x - 1) + (y - 1) * 3
    return cells[:index] + player + cells[index + 1:]


def main():
    cells = "_________"
    current_player = "X"
    
    while True:
        print_board(cells)
        state = check_state(cells)
        if state != "Game not finished":
            print(state)
            break
        
        while True:
            try:
                x, y = map(int, input("Enter the coordinates: ").split())
                error = is_valid_move(cells, x, y)
                if error:
                    print(error)
                else:
                    break
            except ValueError:
                print("You should enter numbers!")
        
        cells = make_move(cells, x, y, current_player)
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()

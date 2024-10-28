def plot_route(filename):
    grid_size = 12
    directions = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            start_x = int(lines[0].strip())
            start_y = int(lines[1].strip())
            moves = [line.strip() for line in lines[2:] if line.strip()]

            if not (1 <= start_x <= grid_size and 1 <= start_y <= grid_size):
                print("Error: The starting coordinates are outside of the grid")
                return

            current_x, current_y = start_x - 1, start_y - 1
            route_coordinates = [(current_x + 1, current_y + 1)]
            grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
            grid[current_y][current_x] = 'X'

            for move in moves:
                if move in directions:
                    delta_x, delta_y = directions[move]
                    new_x = current_x + delta_x
                    new_y = current_y + delta_y

                    # Check bounds (1-based indexing for user but 0-based for grid)
                    if 1 <= new_x + 1 <= grid_size and 1 <= new_y + 1 <= grid_size:
                        current_x, current_y = new_x, new_y
                        route_coordinates.append((current_x + 1, current_y + 1))
                        grid[current_y][current_x] = 'X'
                    else:
                        print("Error: The route is outside of the grid")
                        return
                else:
                    print("Error: Invalid move direction")
                    return

            for row in grid:
                print(' '.join(row))
            print("Route coordinates:", route_coordinates)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ValueError:
        print("Error: Invalid data in the route instructions file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        filename = input("Enter the next route instructions file or enter STOP to finish: ")
        if filename.strip().upper() == "STOP":
            break
        plot_route(filename)

if __name__ == "__main__":
    main()

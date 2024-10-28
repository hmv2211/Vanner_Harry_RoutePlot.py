import matplotlib.pyplot as plt

# Define the grid size (12x12 grid)
GRID_SIZE = 12

def parse_route_file(file_name):
    """Reads a route from a file and returns the starting position and list of moves."""
    with open(file_name, 'r') as f:
        data = f.read().strip().split()
    if len(data) < 3:
        raise ValueError("Route file format is incorrect. It must contain a start position and directions.")
    
    # Extract the starting coordinates and route directions
    start_x, start_y = int(data[0]), int(data[1])
    moves = data[2:]
    return start_x, start_y, moves

def is_valid_position(x, y):
    """Check if a position is within the grid boundaries."""
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE

def plot_route(start_x, start_y, moves):
    """Processes and plots the drone route if valid; prints an error if out of bounds."""
    x, y = start_x, start_y
    route_x, route_y = [x], [y]  # Lists to store the route coordinates

    for move in moves:
        if move == "N":
            y += 1
        elif move == "S":
            y -= 1
        elif move == "E":
            x += 1
        elif move == "W":
            x -= 1
        else:
            print(f"Error: Invalid move {move}")
            return False

        # Check if the new position is within bounds
        if not is_valid_position(x, y):
            print("Error: The route is outside of the grid")
            return False

        route_x.append(x)
        route_y.append(y)

    # Print the route coordinates
    print("Route coordinates:", list(zip(route_x, route_y)))

    # Plot the route
    plt.plot(route_x, route_y, marker='o', color='b')
    plt.xlim(-1, GRID_SIZE)
    plt.ylim(-1, GRID_SIZE)
    plt.grid(True)
    plt.title("Drone Route")
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.show()
    return True

def main():
    while True:
        # Prompt the user for a route file name
        file_name = input("Enter the next route instructions file or enter STOP to finish: ")
        if file_name.lower() == 'stop':
            print("Exiting the program.")
            break
        
        try:
            start_x, start_y, moves = parse_route_file(file_name)
            if is_valid_position(start_x, start_y):
                valid = plot_route(start_x, start_y, moves)
                if not valid:
                    print("Route plotting failed due to invalid moves.")
            else:
                print("Error: The starting position is outside of the grid.")
        except FileNotFoundError:
            print("Error: File not found. Please enter a valid file name.")
        except ValueError as e:
            print(f"Error: {e}")

# Run the main function
if __name__ == "__main__":
    main()

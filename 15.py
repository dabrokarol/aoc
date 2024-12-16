import numpy as np

LOG = False


def log(*args, **kwargs):
    if LOG:
        print(*args, **kwargs)


def parse_input(file_name="15.in2"):
    try:
        with open(file_name, "r") as f:
            lines = f.read().strip().split("\n")
    except FileNotFoundError:
        print("File not found. Enter input manually (empty line to finish):")
        lines = ""
        while True:
            line = input().strip()
            if line == "":
                break
            lines += "\n" + line

    if not lines:
        raise ValueError("Input is empty.")

    grid = []
    start = 0
    for i, line in enumerate(lines):
        if line.strip():
            grid.append(list(line))
        else:
            start = i
            break
    queue = []
    for i in range(start, len(lines)):
        queue += list(lines[i])

    return grid, queue


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_dir(q):
    if q == ">":
        return DIRS[0]
    if q == "v":
        return DIRS[1]
    if q == "<":
        return DIRS[2]
    if q == "^":
        return DIRS[3]
    else:
        raise ValueError("Invalid direction.")


def move(pos, dir, grid) -> bool:
    pos = tuple(pos)
    log("pd", pos, dir)
    new_pos = pos[0] + dir[0], pos[1] + dir[1]
    log("np", new_pos)
    if grid[new_pos] == "#":
        return False
    elif grid[new_pos] == ".":
        grid[new_pos] = grid[pos]
        grid[pos] = "."
        return True
    elif move(new_pos, dir, grid):
        grid[new_pos] = grid[pos]
        grid[pos] = "."
        return True
    else:
        return False


def move_2_iter(pos, dir, grid) -> bool:
    pos = tuple(pos)
    y, x = pos
    if dir == (0, 1):
        x_1 = x + 1
        while grid[y, x_1] in ("[", "]"):
            x_1 += 1
        if grid[y, x_1] == "#":
            return False
        if grid[y, x_1] == ".":
            grid[y][x + 1 : x_1 + 1] = grid[y][x:x_1]
            grid[y][x] = "."
            return True
    if dir == (0, -1):
        x_1 = x - 1
        while grid[y, x_1] in ("[", "]"):
            x_1 -= 1
        if grid[y, x_1] == "#":
            return False
        if grid[y, x_1] == ".":
            grid[y][x_1:x] = grid[y][x_1 + 1 : x + 1]
            grid[y][x] = "."
            return True
    if dir == (1, 0) or dir == (-1, 0):
        xs_to_check = set({x})
        change_later = {(y + dir[0], x): grid[y, x]}
        change_later[y, x] = "."
        while True:
            y += dir[0]
            barrier_met = False
            to_add = set()
            to_remove = set()

            log("y", y, end=" ")
            log("xs_to_check", xs_to_check, end=" ")
            for xs in xs_to_check:
                if grid[y, xs] == "[":
                    if xs + 1 not in xs_to_check:
                        to_add.add(xs + 1)
                        change_later[y, xs + 1] = "."
                if grid[y, xs] == "]":
                    if xs - 1 not in xs_to_check:
                        to_add.add(xs - 1)
                        change_later[y, xs - 1] = "."
            for x in to_add:
                xs_to_check.add(x)
            for xs in xs_to_check:
                if grid[y, xs] == "#":
                    barrier_met = True
                    break
                if grid[y, xs] in ("[", "]"):
                    change_later[y + dir[0], xs] = grid[y, xs]
                if grid[y, xs] == ".":
                    to_remove.add(xs)
            for x in to_remove:
                xs_to_check.remove(x)

            if barrier_met:
                return False
            if len(xs_to_check) == 0:
                break

            log(xs_to_check)
        for (y, x), val in change_later.items():
            grid[y, x] = val
        return True

    return False


def print_grid(grid):
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            print(grid[y, x], end="")
        print()


def calc_score(grid):
    score = 0
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y][x] in {"O", "["}:
                score += x + 100 * y
    return score


def main():
    grid, queue = parse_input("in/15.in")

    grid = np.array(grid, dtype=str)
    queue = np.array(queue, dtype=str)

    pos = next(
        (i, j)
        for i in range(grid.shape[0])
        for j in range(grid.shape[1])
        if grid[i][j] == "@"
    )
    for q in queue:
        dir = get_dir(q)
        if move(pos, dir, grid):
            log(pos, dir, q)
            pos = pos[0] + dir[0], pos[1] + dir[1]

    print_grid(grid)

    print(calc_score(grid))


def main2():
    grid, queue = parse_input("in/15.in")
    grid = np.array(grid, dtype=str)
    queue = np.array(queue, dtype=str)
    grid2 = np.full((grid.shape[0], grid.shape[1] * 2), " ")

    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y][x] == "#":
                grid2[y][x * 2] = "#"
                grid2[y][x * 2 + 1] = "#"
            if grid[y][x] == ".":
                grid2[y][x * 2] = "."
                grid2[y][x * 2 + 1] = "."
            if grid[y][x] == "O":
                grid2[y][x * 2] = "["
                grid2[y][x * 2 + 1] = "]"
            if grid[y][x] == "@":
                grid2[y][x * 2] = "@"
                grid2[y][x * 2 + 1] = "."
    grid = grid2

    # print_grid(grid)

    pos = next(
        (i, j)
        for i in range(grid.shape[0])
        for j in range(grid.shape[1])
        if grid[i][j] == "@"
    )
    for q in queue:
        dir = get_dir(q)
        if move_2_iter(pos, dir, grid):
            grid[pos] = "."
            pos = tuple(np.add(pos, dir))
            grid[pos] = "@"

        log(pos, dir, q)
    # print_grid(grid)

    print(calc_score(grid))


LOG = False

if __name__ == "__main__":
    main()
    main2()

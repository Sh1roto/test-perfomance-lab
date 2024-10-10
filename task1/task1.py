import sys

def circular_array_path(n, m):
    path = []
    current_pos = 0
    while current_pos not in path:
        path.append(current_pos + 1)
        current_pos = (current_pos + m) % n
    return ''.join(map(str, path))

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = circular_array_path(n, m)
    print(result)
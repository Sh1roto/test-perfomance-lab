import sys

def point_position(circle_file, points_file):
    with open(circle_file, 'r') as f:
        cx, cy = map(float, f.readline().split())
        radius = float(f.readline())

    with open(points_file, 'r') as f:
        points = [tuple(map(float, line.split())) for line in f]

    results = []
    for x, y in points:
        distance_sq = (x - cx) ** 2 + (y - cy) ** 2
        if abs(distance_sq - radius ** 2) < 1e-9:
            results.append(0)  # На окружности
        elif distance_sq < radius ** 2:
            results.append(1)  # Внутри
        else:
            results.append(2)  # Снаружи

    return results

if __name__ == "__main__":
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    positions = point_position(circle_file, points_file)
    for pos in positions:
        print(pos)
with open("advent-of-code/2025/day9/input.txt", "r") as f:
    coords = [list(map(int, c.split(','))) for c in f.read().splitlines()]

# As in part 1, enumerate all rectangles and sort by area descending
area = {}

for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        area[(i, j)] = (abs(coords[i][0] - coords[j][0]) + 1) * \
                       (abs(coords[i][1] - coords[j][1]) + 1)

area_sort = dict(sorted(area.items(), key=lambda x: x[1], reverse=True))

# Check for validility of rectangles
# There are 2 ways to fail:
# 1. Edge of polygon crosses the interior of rectangle
# 2. Center of rectangle is outside the polygon

def is_edge_intersect(edge, rect):
    """
    Params
    ------
        edge : list[list[float]]
            (x, y) coordinates of the 2 endpoints of the edge: [[x1, y1], [x2, y2]]
        rect : list[float]
            x and y coordinates which mark the boundary of the rectangle: [x_min, x_max, y_min, y_max]

    Returns
    -------
        boolean, True if the polygon edge intersects the rectangle, False otherwise
    """
    x1, y1 = edge[0][0], edge[0][1]
    x2, y2 = edge[1][0], edge[1][1]

    edge_x_min, edge_x_max = min(x1, x2), max(x1, x2)
    edge_y_min, edge_y_max = min(y1, y2), max(y1, y2)
    rect_x_min, rect_x_max, rect_y_min, rect_y_max = rect[0], rect[1], rect[2], rect[3]

    # Vertical
    if edge_x_min == edge_x_max:
        if edge_x_min <= rect_x_min or edge_x_min >= rect_x_max:
            return False
        if edge_y_min >= rect_y_max or edge_y_max <= rect_y_min:
            return False
        return True

    # Horizontal
    else:
        if edge_y_min <= rect_y_min or edge_y_min >= rect_y_max:
            return False
        if edge_x_min >= rect_x_max or edge_x_max <= rect_x_min:
            return False
        return True

def is_interior_point(point, polygon):
    """
    Params
    ------
        point : list[float]
            (x, y) coordinates of the point
        polygon : list[list[float]]
            polygon vertices' (x, y) coordinates
    
    Returns
    -------
        boolean, True if the point is inside the polygon, False otherwise
    """
    x, y = point[0], point[1]
    cnt = 0

    for i in range(len(polygon)):
        x1, y1 = polygon[i][0], polygon[i][1]
        x2, y2 = polygon[(i+1) % len(polygon)][0], polygon[(i+1) % len(polygon)][1]

        if x1 != x2:
            continue

        y_max = max(y1, y2)
        y_min = min(y1, y2)

        if y >= y_min and y < y_max and x < x1:
            cnt += 1
    
    if cnt % 2 == 1:
        return True
    
    else:
        return False

for (idx1, idx2) in area_sort:
    rect_x_min, rect_x_max = min(coords[idx1][0], coords[idx2][0]), max(coords[idx1][0], coords[idx2][0])
    rect_y_min, rect_y_max = min(coords[idx1][1], coords[idx2][1]), max(coords[idx1][1], coords[idx2][1])
    rect = [rect_x_min, rect_x_max, rect_y_min, rect_y_max]
    rect_center = [(rect_x_min + rect_x_max) / 2, (rect_y_min + rect_y_max) / 2]

    if not is_interior_point(rect_center, coords):
        continue
    
    for i in range(len(coords)):
        edge = [coords[i], coords[(i+1) % len(coords)]]

        is_valid = True
        if is_edge_intersect(edge, rect):
            is_valid = False
            break
    
    if is_valid:
        print(area_sort[(idx1, idx2)])
        break
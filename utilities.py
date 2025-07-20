import math
import pygame

def is_circle(path, tolerance=0.4):
    if len(path) < 30:
        return False  # Not enough points to form a circle

    # Find the center of the path
    xs, ys = zip(*path)  # Split into separate x and y lists
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)

    # Measure distance of each point from the center
    distances = [math.hypot(x - cx, y - cy) for x, y in path]
    avg_radius = sum(distances) / len(distances)

    # Measure how much each point’s radius deviates from the average
    radius_variance = sum((d - avg_radius) ** 2 for d in distances) / len(distances)
    circularity = radius_variance / (avg_radius ** 2 + 1e-5)  # Normalize

    # Check that the path loops back to the starting point
    start = pygame.Vector2(path[0])
    end = pygame.Vector2(path[-1])
    loop_closed = start.distance_to(end) < avg_radius * 0.5

    # Return True if shape is circular enough *and* it's closed
    return circularity < tolerance and loop_closed


def calculate_circularity(path):
    if len(path) < 10:
        return float('inf')  # not enough data, return worst possible

    # Calculate the center of the path
    xs, ys = zip(*path)
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)

    # Calculate distance of each point from center
    distances = [math.hypot(x - cx, y - cy) for x, y in path]
    avg_radius = sum(distances) / len(distances)

    # Measure variance in distances
    radius_variance = sum((d - avg_radius) ** 2 for d in distances) / len(distances)

    # Normalize variance to make it scale-invariant
    circularity = radius_variance / (avg_radius ** 2 + 1e-5)

    return circularity


def circularity_to_accuracy(circularity, tolerance=0.4):
    # Clamp circularity to avoid divide-by-zero or overly harsh grading
    capped = min(circularity, tolerance * 2)

    # Scale: lower circularity = higher accuracy
    raw_score = 1.0 - (capped / (tolerance * 2))  # from 1 to 0
    accuracy = int(raw_score * 100)              # from 100 to 0
    return max(0, min(accuracy, 100)) / 100
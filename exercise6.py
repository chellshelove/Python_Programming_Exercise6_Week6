import math

def cal_shortest_dist(points):
    # Function to calculate the Euclidean distance between two points
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    # Initialize the shortest distance as a large number
    shortest_dist = float('inf')
    
    # Compare each pair of points to find the shortest distance
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < shortest_dist:
                shortest_dist = dist
                
    return shortest_dist

# Example usage
points = [(3, 4), (0, 1), (5, 7)]

result = cal_shortest_dist(points)
print("Shortest distance between two points:", result)
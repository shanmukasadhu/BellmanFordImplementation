# Bellman-Ford Algorithm Implementation

## Overview
This project implements the **Bellman-Ford Algorithm** to find the shortest path from a source node to all other nodes in a weighted graph. The algorithm is particularly useful for graphs that contain negative weight edges and detects negative weight cycles.

## Features
- Handles graphs with positive and negative edge weights
- Detects the shortest path from a given source node
- Runs in **O(V * E)** time complexity

## Algorithm Explanation
1. Initialize the distances dictionary with infinity (`inf`) for all nodes except the source node, which is set to `0`.
2. Relax all edges **(V-1) times**, where `V` is the number of vertices:
   - Iterate through all edges and update the shortest known distance to each node.
3. Print the shortest distances from the source node to all other nodes.

## Graph Representation
The graph is represented using an **adjacency list**, where each node maps to a list of tuples containing its neighboring nodes and the edge weights:

```python
adjacency_list = {
    "A": [("B", 2), ("D", 8)],
    "B": [("A", 2), ("D", 5), ("E", 6)],
    "C": [("E", 9), ("F", 3)],
    "D": [("A", 8), ("B", 5), ("E", 3), ("F", 2)],
    "E": [("B", 6), ("D", 3), ("C", 9), ("F", 1)],
    "F": [("D", 2), ("E", 1), ("C", 3)]
}
```

## Implementation
### Step 1: Initialize Distances
```python
distances = {"A": 0, "B": float("inf"), "C": float("inf"), "D": float("inf"), "E": float("inf"), "F": float("inf")}
```

### Step 2: Relax All Edges (V-1) Times
```python
for i in range(len(adjacency_list) - 1):
    for node in adjacency_list:
        for neighbor, weight in adjacency_list[node]:
            if distances[node] != float('inf') and distances[neighbor] > distances[node] + weight:
                distances[neighbor] = distances[node] + weight
```

### Step 3: Output the Shortest Distances
```python
print(distances)
```

## Example Output
```
{'A': 0, 'B': 2, 'D': 7, 'E': 9, 'F': 9, 'C': 12}
```

## Limitations
- **Does not check for negative weight cycles**. To extend the implementation, an additional pass should be added to detect cycles.

## Future Improvements
- Add negative weight cycle detection
- Implement path reconstruction to track the shortest path

## Author
This implementation was created for learning purposes and demonstrates the Bellman-Ford algorithm in Python.

---

Feel free to use and modify this implementation as needed!





# ----------- Initialization --------- #


# Assign neighbors with edge weights
adjacency_list = {
    "A": [("B", 2), ("D", 8)],
    "B": [("A", 2), ("D", 5), ("E", 6)],
    "C": [("E", 9), ("F", 3)],
    "D": [("A", 8), ("B", 5), ("E", 3), ("F", 2)],
    "E": [("B", 6), ("D", 3), ("C", 9), ("F", 1)],
    "F": [("D", 2), ("E", 1), ("C", 3)]
}

# ----------- Bellman-Ford's Algorithm --------- #


# Set source node to 0, in this case 0
distances = {"A":0, "B": float("inf"), "C": float("inf"), "D": float("inf"), "E": float("inf"), "F": float("inf")}

# Iterate every n-1 iterations
for i in range(len(adjacency_list)-1):
    # Iterate through each node
    for node in adjacency_list:
        # Iterate through each neighbhor
        for neighbhor, weight in adjacency_list[node]:
            # If the neighbhor hasn't been discovered, ignore it.
            # if the distance to the neighbhor is greater than the distance to the node + edge
            if distances[node] != float('inf') and distances[neighbhor] > distances[node]+weight:
                # Change it
                distances[neighbhor] = distances[node]+weight


print(distances)

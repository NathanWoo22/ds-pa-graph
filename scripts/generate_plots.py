import matplotlib.pyplot as plt
import numpy as np


with open("data_info.txt", "r+") as ifile:
    lines = ifile.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.strip().split()
        lines[i] = [float(x) for x in lines[i]]

    
    lines = lines[:-1]
    nodes = np.array([line[0] for line in lines])
    edges = np.array([line[1]/1000 for line in lines])
    time = np.array([line[2] for line in lines])
    print(nodes)
    print(edges)
    print(time)
    plt.figure(figsize=(9, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(nodes, time)
    plt.title("Nodes vs Time")
    plt.xlabel("Nodes (number)")
    plt.ylabel("Time (s)")

    plt.subplot(1, 2, 2)
    plt.plot(edges, time)
    plt.title("Edges vs Time")
    plt.xlabel("Edges (number in thousands)")
    plt.ylabel("Time (s)")
    # print(nodes, time)

    plt.savefig("nodes_time.png")
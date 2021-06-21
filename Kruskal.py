class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0, 1, 10], ]

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort all the edges from low weight to high
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # Keep adding edges until we reach all vertices.
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            temp_w = 0
            if temp_w < w:
                temp_w += w

            # Take the edge with the lowest weight and add it to the spanning tree.
            # If adding the edge created a cycle,
            # then reject this edge.
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        minimum_cost = 0
        # central_hub_print_index = 0
        for u, v, weight in result:
            # using this as the printing is gonna start
            # from root element and thus printing it once as central hub
            # if central_hub_print_index < 1:
            #     # print("central Hub: ", u)
            #     central_hub_print_index += 1
            minimum_cost += weight
            print("%d - %d: %d" % (u, v, weight))
        print("Kruskal's Minimum Spanning Tree Cost:", minimum_cost)

    def find_max_spanning_tree(self):
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort all the edges from low weight to high
        self.graph = sorted(self.graph, key=lambda item: item[2], reverse=True)

        parent = []
        rank = []
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # Keep adding edges until we reach all vertices.
        while e < self.V - 1:

            # Step 2: Pick the largest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            temp_w = 0
            if temp_w < w:
                temp_w += w

            # Take the edge with the highest weight and add it to the spanning tree. If adding the edge created a cycle,
            # then reject this edge.
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        maximum_cost = 0
        for u, v, weight in result:
            maximum_cost += weight
            print("%d - %d: %d" % (u, v, weight))
        print("Maximum Spanning Tree Cost:", maximum_cost)

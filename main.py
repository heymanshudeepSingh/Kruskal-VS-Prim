#  https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
#  https://www.programiz.com/dsa/kruskal-algorithm
# ========================================================================
#  By Singh
#  This program foreshadows kruskal algorithm
from Kruskal import Graph
from Prim import Graph as PrimsGraph
import random
import time


def randomly_generate_kruskal_graphs(number_of_graphs):
    graph = Graph(10)
    count = 0
    for total_graphs in range(0, number_of_graphs):
        for i in range(0, 100):
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c_weight = random.randint(1, 100)
            graph.add_edge(a, b, c_weight)
        count += 1
        graph.kruskal_algo()
    print("count", count)


def manual_kruskal():
    vertices = input("Enter the number of vertices: ")
    while not vertices.isdigit():
        vertices = input("\033[93mEnter Valid number of vertices\033[0m: ")
    vertices = int(vertices)
    graph = Graph(vertices)
    for i in range(0, vertices * vertices):
        a = random.randint(0, vertices - 1)
        b = random.randint(0, vertices - 1)
        c_weight = random.randint(1, 100)
        graph.add_edge(a, b, c_weight)
    graph.kruskal_algo()


def manual_prim():
    vertices = input("Enter the number of vertices: ")
    while not vertices.isdigit():
        vertices = input("\033[93mEnter Valid number of vertices\033[0m: ")
    vertices = int(vertices)
    graph = PrimsGraph(vertices)
    for i in range(0, vertices * vertices):
        a = random.randint(0, vertices - 1)
        b = random.randint(0, vertices - 1)
        c_weight = random.randint(1, 100)
        graph.add_edge(a, b, c_weight)
    graph.PrimMST()


def randomly_generate_prims_graphs(number_of_graphs):
    graph = PrimsGraph(10)
    for total_graphs in range(0, number_of_graphs):
        for i in range(0, 100):
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c_weight = random.randint(1, 100)
            graph.add_edge(a, b, c_weight)
        graph.PrimMST()


def kruskal_vs_prim():
    number_of_graphs = input("Enter the number of number of graphs to generate: ")
    while not number_of_graphs.isdigit():
        number_of_graphs = input("\033[93mEnter Valid number of graphs to generate\033[0m: ")
    number_of_graphs = int(number_of_graphs)
    vertices = input("Enter the number of vertices: ")
    while not vertices.isdigit():
        vertices = input("\033[93mEnter Valid number of vertices\033[0m: ")
    vertices = int(vertices)
    graph1 = Graph(vertices)
    graph2 = PrimsGraph(vertices)
    total_time_kruskal = time.time()
    total_time_prim = time.time()
    for total_graphs in range(0, number_of_graphs):
        for i in range(0, vertices * vertices):
            a = random.randint(0, vertices - 1)
            b = random.randint(0, vertices - 1)
            c_weight = random.randint(1, 100)
            graph1.add_edge(a, b, c_weight)
            graph2.add_edge(a, b, c_weight)
        start_time1 = time.time()
        graph1.kruskal_algo()
        end_time1 = time.time()
        total_time_kruskal += end_time1 - start_time1
        start_time2 = time.time()
        graph2.PrimMST()
        end_time2 = time.time()
        total_time_prim += end_time2 - start_time2
    print("Total Time for Kruskal's algorithm: ", total_time_kruskal)
    print("Total Time for Prim's algorithm: ", total_time_prim)


if __name__ == '__main__':
    number_of_graphs_to_generate = 100

    is_valid = False
    while not is_valid:
        user_input = input("1. Generate 100 randomized graphs using\033[96m Kruskal's\033[0m algorithm\n"
                           "2. Generate 100 randomized graphs using\033[96m Prim's'\033[0m algorithm\n"
                           "3. Manually create \033[96m Kruskal's\033[0m graph using user input Vertices\n"
                           "4. Manually create \033[96m Prim's'\033[0m graph using user input Vertices\n"
                           "5. Create Multiple Kruskal and Prim graphs\n"
                           "0. \033[96mEXIT\033[0m \n"
                           "=")

        if user_input.isdigit() and (0 <= int(user_input) <= 5):
            if user_input == "1":
                start_time = time.time()
                randomly_generate_kruskal_graphs(number_of_graphs_to_generate)
                print("--- %s seconds ---" % (time.time() - start_time))

            if user_input == "2":
                start_time = time.time()
                randomly_generate_prims_graphs(number_of_graphs_to_generate)
                print("--- %s seconds ---" % (time.time() - start_time))

            if user_input == "3":
                start_time = time.time()
                manual_kruskal()
                print("--- %s seconds ---" % (time.time() - start_time))

            if user_input == "4":
                start_time = time.time()
                manual_prim()
                print("--- %s seconds ---" % (time.time() - start_time))

            if user_input == "5":
                kruskal_vs_prim()

            if user_input == "0":
                print("Exiting Program!")
                is_valid = True
        else:
            print("Invalid Input Received!")
            user_input = input("1. Generate 100 randomized graphs using\033[96m Kruskal's\033[0m algorithm\n"
                               "2. Generate 100 randomized graphs using\033[96m Prim's'\033[0m algorithm\n"
                               "3. Manually create \033[96m Kruskal's\033[0m graph using user input Vertices\n"
                               "4. Manually create \033[96m Prim's'\033[0m graph using user input Vertices\n"
                               "5. Create Multiple Kruskal and Prim graphs\n"
                               "0. \033[96mEXIT\033[0m \n"
                               "=")

    # Uncomment to see max spanning tree as well
    # g.find_max_spanning_tree()

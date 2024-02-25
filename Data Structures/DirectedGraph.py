from Dictionary import OptimizedDictionary
from ArrayList import ArrayList
import networkx as nx
import matplotlib.pyplot as plt
from Set import Set
from tqdm import tqdm
from Stack import Stack

        
class OptimizedDirectedGraph:
    def __init__(self):
        self.graph = OptimizedDictionary(35000)
        
    def selection_sort(self):
        n = self.itemCount

        for i in tqdm(range(n),desc="Siralaniyor"):
            min_index = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        
    def show_graph(self):
        G = nx.Graph()

        for node, neighbors in self.graph.toDict().items():
            G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G)  

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
        plt.show()

    def add_vertex(self, vertex):
        if vertex not in self.graph.keys:
            a = ArrayList()
            self.graph.put(vertex,a)


    def add_edge(self, start, end):

        a = self.graph.get(start)
        a.add(end)
        self.graph.put(start,a)
        
    def dfs(self, start, visited=None):
        if visited is None:
            visited = Set()

        if start not in visited:
            print(start)
            
            visited.add(start)

            neighbors = self.graph.get(start)
            
            for neighbor in neighbors:
                self.dfs(neighbor, visited)
                
    def dfs_iterative(self, start):
        
        visited = set()
        stack = Stack()
        stack.push(start)

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                if(current_node is None):
                    break
                
                print(current_node)
                visited.add(current_node)

                neighbors = self.graph.get(current_node)
                stack.extend(neighbors)

    def display_graph(self):
        mainstr = ""
        for vertex in self.graph.keys:
            if vertex is not None:
                neighbors = ", ".join(map(str, self.graph.get(vertex)))
                if(neighbors!=""):
                    mainstr+=f"{vertex} -> {neighbors}\n"
                
        return mainstr
            
            
if __name__=="__main__":
    
    gr = OptimizedDirectedGraph()
    gr.add_vertex("a")
    gr.add_vertex("b")
    gr.add_vertex("c")

    gr.add_edge("a","b")
    gr.add_edge("a","c")
    gr.add_edge("b","c")

    print(gr.display_graph())
    
    gr.dfs_iterative("a")
            

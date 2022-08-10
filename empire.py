import numpy as np
import matplotlib.pyplot as plt
import node

class Empire:
    # Plot is 1000 x 1000
    counter = 0

    def __init__(self):
        self.node_count = 100
        Empire.counter += 1
        self.counter = Empire.counter
        self.node_list = []

    def generate_nodes(self):
        node_list = []
        sigma = 100 

        # generate multidimensional gaussian
        def gauss_2d(x_mu, y_mu, sigma, node_count):
            x = sigma*np.random.randn(node_count) + x_mu
            y = sigma*np.random.randn(node_count) + y_mu
            return (x,y)

        for i in range(self.node_count):
            if self.counter == 1: # bottom-left
                x_mu = 250
                y_mu = 250
            elif self.counter == 2: # top-right
                x_mu = 750
                y_mu = 750
            elif self.counter == 3: # top-left
                x_mu = 250
                y_mu = 750
            elif self.counter == 4: # bottom-right
                x_mu = 750
                y_mu = 250
            else:
                raise Exception("Empire count must be between 1 and 4")
            x,y = gauss_2d(x_mu, y_mu, sigma, self.node_count)
            new_node = Node(x,y,self.counter)
            node_list.append(new_node)

        self.node_list = node_list
        
    def __str__(self):
        return "Empire " + str(self.counter) + ": " + str(self.node_count)

    def get_nodes(self):
        return self.node_list

    def print_nodes(self):
        print(self.node_list)



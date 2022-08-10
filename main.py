import empire
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Initialize Empires
    empire1 = empire.Empire()
    empire1.generate_nodes()
    empire2 = empire.Empire()
    empire2.generate_nodes()

    print(empire1)

    # Plot scatterplot
    empire1_node_list = empire1.get_nodes()
    empire2_node_list = empire2.get_nodes()

    # Begin Game


    # Declare Winner + Show Statistics





if __name__ == "__main__":
    main()

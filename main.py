from tabulate import tabulate

if __name__ == "__main__":
    table = [(a, b) for a, b in zip(range(10, 20), range(20, 30))]
    print(tabulate(table))
    

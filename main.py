from agent import MT, CB, NA, BFS, a_star_search
from board import Board
import numpy as np
import time

def main():

    string_dict = {MT: "Misplaced Tiles heuristic", CB: "City-Block Distance heuristic", NA: "Non-Admissible heuristic", BFS: "Breadth-First Search"}

    for test in [MT, CB, NA, BFS]:
        print("Testing %s..." % string_dict[test])
        for m in [10,20,30,40,50]:
            sum_cput = 0
            sum_solLen = 0
            sum_nodeS = 0
            for seed in range(0,10): # Sets the seed of the problem so all students solve the same problems
                board = Board(m, seed)
                
                start =  time.process_time()
                data = a_star_search(board, test)
                end =  time.process_time()
                solution_cpu_time = end-start

                sum_cput += solution_cpu_time
                sum_solLen += len(data[1])
                sum_nodeS += data[0]
            print("= M=%d" % m)
            print("== Average CPU Time: %0.3f" % (sum_cput / 10))
            print("== Average Solution Length: %0.3f" % (sum_solLen / 10))
            print("== Total nodes searched: %d" % sum_nodeS)
            print()
        print()

if __name__ == "__main__":
    main()

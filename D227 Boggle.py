# This problem was asked by Facebook.

# Boggle is a game played on a 4 x 4 grid of letters. 
# The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, 
# using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.


# This is a very basic, almost brute force way of doing it. I didn't realize that corner letters are also considered adjacent.
# This should be solved using DFS

def boggleSolver(board, dic):
    used = [[0 for i in range(4)] for i in range(4)]
    word = ""
    res = []
    for i in range(4):
        for j in range(4):
            for k in range(j,4):
                if used[i][k] == 1:
                    if k == 3:
                        word = ""
                    continue
                else:
                    word += board[i][k]
                    
                    if word in dic:
                        
                        for t in range(j, k + 1):
                            used[i][t] = 1
                        res.append(word)
                        word = ""
                    else:
                        if k == 3:
                            word = ""
    for j in range(4):
        for i in range(4):
            for k in range(i,4):
                if used[k][j] == 1:
                    if k == 3:
                        word = ""
                    continue
                else:
                    word += board[k][j]
                    
                    if word in dic:
                        
                        for t in range(i, k + 1):
                            used[t][i] = 1
                        res.append(word)
                        word = ""
                    else:
                        if k == 3:
                            word = ""
    return len(res)
    
board = [
    ["h", "i", "x", "d"], 
    ["s", "a", "y", "d"], 
    ["u", "m", "e", "m"], 
    ["s", "t", "s", "o"]]
dic = {"hi", "say", "us", "mem", "so"}
print(boggleSolver(board,dic))
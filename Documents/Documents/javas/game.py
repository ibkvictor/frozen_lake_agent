
import math

def minimax(postion ,depth, maximizing_player):
    if depth == 0 and end_game == True:
        return eval
    
    if maximizing_player:
        alpha = -math.inf
        for b in list:
            eval = minimax(child, depth -1, False)
            alpha = max(eval, alpha)
        return alpha
            
    else:
        beta = math.inf
        for b in list:
            eval = minimax(child, depth -1, True)
            beta = max(eval, beta)
        return beta

class Node:
    depth = 0      
    def binary_search(self,tree):
        if type(tree) != list or type(tree) != list or tuple or type(tree) != list or dict:
            return tree, depth
        
        else:
            for item in tree:
                if isinstance(item, list):
                    self.depth +=1
                    return binary_search(item),self.depth

                else:
                    self.depth += 1
                    return item, self.depth

#state machines

class SM:
    pass

class accumulator(SM):
    startstate = 0
    def work(self, state , inps):
        if state == 0 and inps == 'a':
            return (True, 1)
        elif state == 1 and inps == 'b':
            return (True, 2)
        elif state == 2 and inps == 'c':
            return (True, 0)
        else:
            return (False, 1)

print (math.inf)

# transposer performs the accumulators job together as a whole
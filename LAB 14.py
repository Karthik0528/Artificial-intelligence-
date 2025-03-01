def alpha_beta_pruning(depth, node_index, is_maximizing, scores, alpha, beta, h):
    if depth == h:
        return scores[node_index]
    
    if is_maximizing:
        best = float('-inf')
        for i in range(2):
            val = alpha_beta_pruning(depth+1, node_index*2+i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta_pruning(depth+1, node_index*2+i, True, scores, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Input: Leaf node values
scores = [3, 5, 6, 9, 1, 2, 0, -1]
h = 3  # Height of the tree

optimal_value = alpha_beta_pruning(0, 0, True, scores, float('-inf'), float('inf'), h)
print("The optimal value is:", optimal_value)

def minimax (depth, nodeindex, ismax, scores, h):
    if depth == h:
        return scores[nodeindex]
    
    if ismax:
        return max(minimax(depth + 1, nodeindex * 2, False, scores, h),
                   minimax(depth + 1, nodeindex * 2 + 1, False, scores, h))
    else:
        return min(minimax(depth + 1, nodeindex * 2, True, scores, h),
                   minimax(depth + 1, nodeindex * 2 + 1, True, scores, h))
        
scores=list(map(int, input("Enter the scores of the leaf nodes separated by space: ").strip().split()))
h=3
result=minimax(0, 0, True, scores, h)
print("The optimal value is:", result)

import math

# Alpha-Beta Pruning function
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):

    # Base condition: leaf node
    if depth == height:
        return values[nodeIndex]

    # MAX player
    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best

    # MIN player
    else:
        best = math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best


# Main program
values = list(map(int, input("Enter 8 leaf node values: ").split()))

height = 3

alpha = -math.inf
beta = math.inf

result = alpha_beta(0, 0, True, values, alpha, beta, height)

print("\nThe optimal value is:", result)
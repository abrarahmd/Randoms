import random

def gameOver(position):
    return sum(position)

def alpha_beta_pruning(position, depth, alpha, beta, maximizingPlayers):
    if depth == 0:
        return static evaluation of position
    if maximizingPlayers != True:
        minEval = float('inf')
        for each child of position:
            eval = minimax(child, depth - 1, alpha, beta, true)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return minEval
        
    else:
        
        maxEval = float('-inf')
        for each child of position:
            eval = minimax(child, depth -1, alpha, beta, false)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return maxEval


stdID = input("Enter your Student ID: \n")
random_points = []
for i in range(8):
    random_points.append(random.randint(1, 100))
print(f'Generated 8 random points between the minimum and maximum point limits: {random_points}')

pointsWin = random.randint(1, 100)

print(f'Total points to win: {pointsWin}')

achievedPoints = alpha_beta_pruning(random_points, 3, float('-inf'), float('inf'), True)
print(achievedPoints)
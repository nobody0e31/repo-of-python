if __name__ == '__main__':
    # 1. Read the number of scores (n)
    n = int(input())
    
    # 2. Read the space-separated scores and convert them into a list of integers
    scores = list(map(int, input().split()))
    
    # 3. Convert the list to a 'set' to remove any duplicate scores
    unique_scores = set(scores)
    
    # 4. Remove the absolute highest score from the set
    unique_scores.remove(max(unique_scores))
    
    # 5. The new highest score is the runner-up!
    print(max(unique_scores))
from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin,0))
    visited = {}
    for word in words:
        visited[word] = False
    
    while queue:
        x, step = queue.popleft()
        if x == target:
            return step
        for word in words:
            if visited[word]:
                continue
            cnt = 0
            for i in range(len(begin)):
                if x[i] == word[i]:
                    cnt +=1
            if cnt == len(begin)-1:
                visited[word] = True
                queue.append((word,step+1))
    
    return 0

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
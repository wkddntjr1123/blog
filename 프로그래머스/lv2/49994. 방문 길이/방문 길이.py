def solution(dirs):
    answer = 0
    x = y = 0
    visited = set()
    for op in dirs :
        if op == "U" and x < 5: 
            visited.add((x,y,x+1,y))
            visited.add((x+1,y,x,y))
            x += 1
        elif op == "D" and x > -5 :
            visited.add((x-1,y,x,y))
            visited.add((x,y,x-1,y))
            x -= 1
        elif op == "R" and y < 5 :
            visited.add((x,y+1,x,y))
            visited.add((x,y,x,y+1))
            y += 1
        elif op == "L" and y > -5 :
            visited.add((x,y-1,x,y))
            visited.add((x,y,x,y-1))
            y -= 1
    return len(visited)//2
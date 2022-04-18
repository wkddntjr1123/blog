def solution(skill, skill_trees):
    answer = 0
    table = {}
    for i,v in enumerate(skill):
        table[v] = i
    for s in skill_trees :
        cur = 0
        valid = True
        for char in s :
            if char in table :
                if table[char] != cur :
                    valid = False
                    print(s,char)
                    break
                cur += 1
        if valid :
            answer += 1
    return answer
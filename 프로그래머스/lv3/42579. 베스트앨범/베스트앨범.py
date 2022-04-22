from collections import defaultdict,Counter
def solution(genres, plays) :
    answer = []
    counter = Counter()
    table = defaultdict(list)
    for i in range(len(genres)) :
        counter[genres[i]] += plays[i]
        table[genres[i]].append((plays[i],i))
    for key in table :
        table[key].sort(key=lambda x:(-x[0],x[1]))
    for genre, _ in counter.most_common() :
        for i in range(2 if len(table[genre])>=2 else 1):
            answer.append(table[genre][i][1])
    return answer
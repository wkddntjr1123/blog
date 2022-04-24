from sys import maxsize

def solution(sticker):
    answer = 0
    if len(sticker) <= 3:
        return max(sticker)
    # 첫 번째를 선택하면(0) 마지막을 선택 불가, 두번째를 선택하면(1) 마지막을 선택 가능
    table = [[0, 0] for _ in range(len(sticker)+3)]
    table[0][0] = sticker[0]
    table[1][1] = sticker[1]
    table[2][0] = sticker[0] + sticker[2]
    table[2][1] = sticker[2]
    for i in range(3, len(sticker)) :
        table[i][0] = max(table[i-2][0] + sticker[i], table[i-3][0] + sticker[i], table[i-1][0]) 
        table[i][1] = max(table[i-2][1] + sticker[i], table[i-3][1] + sticker[i], table[i-1][1]) 
    table[len(sticker)-1][0] = 0 # 첫 번째 선택(0) 시 마지막 선택 불가능
    
    return max(map(max,table))
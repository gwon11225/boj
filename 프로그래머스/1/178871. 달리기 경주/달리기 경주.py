def solution(players, callings):
    dic = dict()
    for i, data in enumerate(players):
        dic[i] = data
        dic[data] = i
    
    for i in callings:
        winner = dic[i]
        loser = dic[i] - 1
        players[winner], players[loser] = players[loser], players[winner]
        dic[winner] = players[winner]
        dic[loser] = players[loser]
        dic[players[winner]] += 1
        dic[players[loser]] -= 1
        
    return players
def solution(players, callings):
    ranks = {players[i]:i+1 for i in range(len(players))}
    names = {rank:name for name, rank in ranks.items()}
    for calling in callings:
        low_rank = ranks[calling]
        hign_rank = low_rank - 1
        overtaken = names[hign_rank]
        names[hign_rank], names[low_rank] = names[low_rank], names[hign_rank]
        ranks[overtaken], ranks[calling] = ranks[calling], ranks[overtaken]
    answer = [name for name in names.values()]
    return answer
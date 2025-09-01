import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        # 배열에서 꺼낸 원소가 스코빌 지수 K 이상이면 반복문을 종료
        if min1 >= K:
            break
        # 배열의 길이가 0이 되면 모든 음식의 스코빌 지수를 K 이상으로 만들수 없으므로 반복을 종료
        elif len(scoville) == 0:
            count = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + min2 * 2
        heapq.heappush(scoville, new_scoville)
        count += 1
    return count
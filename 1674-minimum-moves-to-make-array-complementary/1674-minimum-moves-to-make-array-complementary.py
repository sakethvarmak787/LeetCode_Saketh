class Solution:
    def minMoves(self, a: List[int], k: int) -> int:
        p = [*zip(a[:len(a)//2],a[::-1])]
        z,minn,maxx = Counter(map(sum,p)),*map(sorted,zip(*map(sorted,p)))
        return min(len(a)-bisect_left(minn,c)+bisect_left(maxx,c-k)-z[c]
            for c in range(2,2*k+1))
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        items = list(count.items())
        items.sort(key = lambda a: (-a[1], a[0]))
        return list(map(lambda c: c[0], items[:k]))
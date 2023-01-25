class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        custom_comparator = lambda x: x[k]
        score.sort(key = custom_comparator, reverse = True)
        return score
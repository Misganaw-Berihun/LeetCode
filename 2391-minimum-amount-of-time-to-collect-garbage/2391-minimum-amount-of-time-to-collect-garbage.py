class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_occurence = defaultdict(int)
        prefix_size = len(travel) + 1
        garbage_size = len(garbage)
        count = 0
        
        prefix = [0 for i in range(prefix_size)]
        for idx in range(1, prefix_size):
            prefix[idx] += (prefix[idx-1] + travel[idx-1])
        
        for idx, house in enumerate(garbage):
            count += len(house)
            for type_of_garbage in house:
                last_occurence[type_of_garbage] = idx
        
        min_minutes = count
        for type_of_garbage in last_occurence:
            min_minutes += (prefix[last_occurence[type_of_garbage]])
        
        return min_minutes
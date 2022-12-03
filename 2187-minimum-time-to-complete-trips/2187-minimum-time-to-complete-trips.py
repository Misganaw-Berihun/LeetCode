class Solution:
    def can_made_trip(self, time,  total_trips, cur_time):
        num_trips = 0
        for i in range(len(time)):
            time_needed = cur_time // time[i]
            num_trips += time_needed
        return num_trips >= total_trips

    def binary_search(self, time, total_trips):
        left, right = 1, 10**14

        while left < right:
            mid = left + (right - left) // 2
            
            if self.can_made_trip(time, total_trips,  mid):
                right = mid
            else:
                left = mid + 1
                
        return left
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return self.binary_search(time, totalTrips)
        
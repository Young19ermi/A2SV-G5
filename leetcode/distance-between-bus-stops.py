class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, end: int) -> int:
        thesum = sum(distance)
        clockwise = sum(distance[min(start,end):max(start,end)])
        anticlockwise = thesum - clockwise
        return min(clockwise, anticlockwise)

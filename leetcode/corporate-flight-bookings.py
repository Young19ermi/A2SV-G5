class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # flights = []
        # for i in range(len(booking)):
        #     for j in range(len(booking[0])-1):
        #         flights.append(booking[i][j])

        # flights.sort()
        # row1 = flights[0]
        # col = flights[-1]
        # matrix = [[0 for _ in range(col)] for _ in range(row1)]
        # for book in booking:
        #     for i in range(len(book)-1):
        #         matrix[i] += book[len(book)-1]
        # return matrix
        result = [0] * (n + 1)  
        for first, last, seats in bookings:
            result[first - 1] += seats  
            result[last] -= seats  
        for i in range(1, n):
            result[i] += result[i - 1]  

        return result[:-1] 

    










        
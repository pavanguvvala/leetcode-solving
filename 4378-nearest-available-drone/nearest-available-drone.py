class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        min = float('inf')
        ind = -1
        for i in drones :
            dist = abs(i[0]-target[0]) + abs(i[1]-target[1])
            if (dist<=i[2]):
               if (dist<min):
                   min = dist
                   ind = drones.index(i)
        return ind
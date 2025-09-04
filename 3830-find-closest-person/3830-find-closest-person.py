class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distance_person1 = abs (x - z)
        distance_person2 = abs (y - z)

        if distance_person1 < distance_person2:
            return 1
        
        if distance_person2 < distance_person1:
            return 2

        else:
            return 0

        
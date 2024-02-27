# 2126. Destroying Asteroids

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        total = mass
        for i in asteroids:
            if i > total :
                return False
            else :
                total += i

        return True 

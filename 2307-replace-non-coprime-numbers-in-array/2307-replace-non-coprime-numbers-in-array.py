class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        def gcd (a, b):
            return math.gcd(a,b)

        def lcm(a,b):
            if a == 0 or b == 0:
                return 0
            return abs (a * b) // gcd(a,b)

        result = []
        for num in nums:
            result.append(num)

            while len(result) >= 2:
                x = result [-2]
                y = result [-1]

                common_divisor = gcd(x, y)  

                if common_divisor > 1:
                    result.pop ()
                    result.pop ()
                    result.append(lcm(x,y))

                else:
                    #se forem co primos, o loop para
                    break

        return result                     
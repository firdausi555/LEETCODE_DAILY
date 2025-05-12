class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        digit_count = Counter(digits)

        for num in range(100, 1000):
            if num % 2 == 0:  
                num_digits = [int(d) for d in str(num)]
                num_counter = Counter(num_digits)

                if all(num_counter[d] <= digit_count[d] for d in num_counter):
                    result.add(num)

        return sorted(result)

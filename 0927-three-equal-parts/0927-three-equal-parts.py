class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_ones = sum(arr)
        n = len(arr)
        if total_ones == 0:
            return [0, n - 1]
        if total_ones % 3 != 0:
            return [-1, -1]

        ones_per_part = total_ones // 3
        first = second = third = count = 0
        for i, val in enumerate(arr):
            if val == 1:
                if count == 0:
                    first = i
                elif count == ones_per_part:
                    second = i
                elif count == 2 * ones_per_part:
                    third = i
                count += 1

        length_of_part = n - third
        if first + length_of_part <= second and second + length_of_part <= third:
            part1 = arr[first:first + length_of_part]
            part2 = arr[second:second + length_of_part]
            part3 = arr[third:third + length_of_part]
            if part1 == part2 == part3:
                return [first + length_of_part - 1, second + length_of_part]
        return [-1, -1]

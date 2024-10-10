import sys

def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        nums = [int(line.strip()) for line in f]

    result = min_moves_to_equal(nums)
    print(result)
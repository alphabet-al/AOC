from functools import lru_cache, cache
import time

# def main(n):
#     memo = {}
#     start_time = time.time()

# def fib(n, memo = None):
#     if memo is None:
#         memo = {}

#     if n in memo:
#         return memo[n]
    
#     if n <= 2:
#         return 1
    
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)

#     return memo[n]


    # ans = fib(n)
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # return ans, elapsed_time

# ans, elapsed_time = main(999)
# ans = fib(999)
# print(ans)
# print(f"Execution time: {elapsed_time:.6f}")


# def gridTraveler(m, n, memo = None):
#     if memo is None:
#         memo = {}

#     if m == 0 or n == 0: return 0
#     if m == 1 and n == 1: return 1

#     if (m, n) in memo:
#         return memo[(m, n)]
    
#     memo[(m, n)] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)

#     return memo[(m, n)]

# print(gridTraveler(1,1))    # 1
# print(gridTraveler(2,3))    # 3
# print(gridTraveler(3,2))    # 3
# print(gridTraveler(3,3))    # 6
# print(gridTraveler(18,18))  # 233360220

# @cache
# def gridTraveler(m, n):
#     if m == 0 or n == 0: return 0
#     if m == 1 and n == 1: return 1
#     return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

     

# print(gridTraveler(1,1))    # 1
# print(gridTraveler(2,3))    # 3
# print(gridTraveler(3,2))    # 3
# print(gridTraveler(3,3))    # 6
# print(gridTraveler(18,18))  # 233360220

# def canSum(target, numbers, memo = None):
#     if memo is None:
#         memo = {}
    
#     if target in memo:
#         return memo[target]
    
#     if target == 0:
#         return True
    
#     if target < 0:
#         return False
    
#     for num in numbers:
#         new_target = target - num
#         if canSum(new_target, numbers, memo):
#             memo[target] = True
#             return memo[target]
        
#     memo[target] = False
#     return memo[target]

# print(canSum(7, [2, 3]))    # True
# print(canSum(7, [5, 3, 4, 7]))    # True
# print(canSum(7, [2, 4]))    # False
# print(canSum(8, [2, 3, 5]))    # True
# print(canSum(300, [7, 14]))    # False


# @cache
# def canSum(target, numbers):
    
#     if target == 0:
#         return True
    
#     if target < 0:
#         return False
    
#     for num in numbers:
#         new_target = target - num
#         if canSum(new_target, numbers):
#             return True
    
#     return False

# def canSumWrapper(target, numbers):
#     return canSum(target, tuple(numbers))

# # because we can't pass mutable objects to the @cache decorator, we need to convert to a tuple
# # we can do this before we pass to the canSum function or we can create a wrapper function that
# # converts the numbers list into a numbers tuple

# print(canSumWrapper(7, [2, 3]))    # True
# print(canSumWrapper(7, [5, 3, 4, 7]))    # True
# print(canSumWrapper(7, [2, 4]))    # False
# print(canSumWrapper(8, [2, 3, 5]))    # True
# print(canSumWrapper(300, [7, 14]))    # False 

# def howSum(target, numbers, memo = None):    
#     if memo is None:
#         memo = {}

#     if target in memo:
#         return memo[target]
    
#     if target == 0:
#         return []
    
#     if target < 0:
#         return None
    
#     for num in numbers:
#         new_target = target - num
#         new_target_result = howSum(new_target, numbers, memo)
#         if new_target_result != None:
#             memo[target] = [*new_target_result, num]
#             return memo[target]
    
#     memo[target] = None

#     return memo[target]

# print(howSum(0, [1,2,3]))   # []
# print(howSum(8, [2,3,5]))   # [3,5]
# print(howSum(7, [2,4]))     # None
# print(howSum(7, [5,3,4,7]))   # [3,4]
# print(howSum(300, [7, 14])) # None

# @cache
# def howSum(target, numbers):    
#     if target == 0:
#         return []
    
#     if target < 0:
#         return None
    
#     for num in numbers:
#         new_target = target - num
#         new_target_result = howSum(new_target, numbers)
#         if new_target_result != None:
#             return [*new_target_result, num]

#     return None

# def howSumWrapper(target, numbers):
#     return howSum(target, tuple(numbers))


# print(howSumWrapper(0, [1,2,3]))   # []
# print(howSumWrapper(8, [2,3,5]))   # [3,5]
# print(howSumWrapper(7, [2,4]))     # None
# print(howSumWrapper(7, [5,3,4,7]))   # [3,4]
# print(howSumWrapper(300, [7, 14])) # None

@cache
def bestSum(target, numbers):    

    if target == 0:
        return []
    
    if target < 0:
        return None
    
    shortest_combination = None
    for num in numbers:
        new_target = target - num
        new_target_result = bestSum(new_target, numbers)
        if new_target_result != None:
            combination =  [*new_target_result, num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination

def bestSumWrapper(target, numbers):
    return bestSum(target, tuple(numbers))


print(bestSumWrapper(7, [5,3,4,7]))   # [7]
print(bestSumWrapper(8, [2,3,5]))   # [3,5]
print(bestSumWrapper(8, [1,4,5]))   # [4,4]
print(bestSumWrapper(100, [1,2,5,25]))   # [25,25,25,25]

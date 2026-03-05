# Name: Anubhav Kashyap
# Roll No: 2501730017
# Course: B.Tech CSE (AI Ml), 2nd Semester

# Part A: Stack ADT
class StackADT:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

# Part B: Factorial (Recursive)
def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci (Naive)
naive_calls = 0
def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Fibonacci (Memoized)
memo_calls = 0
def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Part C: Tower of Hanoi
def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        print(move)
        return
    hanoi(n - 1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)
    print(move)

    hanoi(n - 1, auxiliary, source, destination, stack)

# Part D: Recursive Binary Search
def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

# Main Function (All Test Cases)
def main():
    print("Factorial Tests:")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) = {factorial(n)}")

    print("\nFibonacci Tests:")
    for n in [5, 10, 20, 30]:
        global naive_calls, memo_calls
        naive_calls = 0
        result_naive = fib_naive(n)
        print(f"\nNaive Fibonacci({n}) = {result_naive}")
        print("Naive Calls =", naive_calls)
        memo_calls = 0
        result_memo = fib_memo(n, {})
        print(f"Memoized Fibonacci({n}) = {result_memo}")
        print("Memo Calls =", memo_calls)

    print("\nTower of Hanoi Tests:")
    stack = StackADT()
    hanoi(3, 'A', 'B', 'C', stack)
    print("\nTotal Moves Stored in Stack:", stack.size())
    print("\nBinary Search Tests:")
    arr = [1,3,5,7,9,11,13]
    for key in [7, 1, 13, 2]:
        index = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key} -> Index: {index}")
    empty_arr = []
    print("Search in empty array:", binary_search(empty_arr, 5, 0, -1))
if __name__ == "__main__":
    main()

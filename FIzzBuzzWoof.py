def solution(N):
    for num in range(1, N + 1):
        if num%3 == 0:
            print("Fizz")
        elif num%5 == 0:
            print("Buzz")
        elif num%7 == 0:
            print("Woof")
        elif num%15 == 0:
            print("FizzBuzz")
        elif num%21 == 0:
            print("FizzWoof")
        elif num%105 == 0:
            print("FizzBuzzWoof")
        else:
            print(num)

solution(100)

# print(solution(int(input("Range : "))))

def countdown(n):
    if n == 0:                # base case
        print("Kickoff!")
        return
    print(n)
    countdown(n - 1)          # recursive case: a smaller problem

countdown(3)

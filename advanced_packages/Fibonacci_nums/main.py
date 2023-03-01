from advanced_packages.Fibonacci_nums.helper import generate_seq, find_num

command = input()

while not command == "Stop":
    data = command.split()
    if data[0] == "Create":
        fib_nums = generate_seq(int(data[-1]))
        print(fib_nums)
    else:
        result = find_num(int(data[-1]), fib_nums)
        print(f"The number - {int(data[-1])} is " f"at index {result}" if isinstance(result, int) else result)

    command = input()
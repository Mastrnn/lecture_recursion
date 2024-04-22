def recursive_nth_fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_nth_fibo(n-2) + recursive_nth_fibo(n-1)


def main():
    n=4
    fib=[recursive_nth_fibo(num)for num in range(1,n+1)]
    print(fib)


if __name__ == "__main__":
    main()

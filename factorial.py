import threading

def factUtil(n):
    if n==0:
        return 1
    return n * factUtil(n-1)

def factorial(n=None, result = None):
    f = factUtil(n)
    print(f)
    result.append(f)


if __name__ == "__main__":
    n=int(input("Enter the number: "))
    result = []
    th = threading.Thread(target=factorial, args=(n, result))
    th.start()
    th.join()
    print("factorial of {} is {}".format(n, result[0]))


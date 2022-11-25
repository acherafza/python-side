import time


def main():
    start = time.time()
    print('Hello World')
    end = time.time()

    print(f'Total time taken to run: {(end - start) * 1000}ms')


if __name__ == '__main__':
    main()

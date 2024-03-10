import multiprocessing

def calculate_square(number):
    """Function to calculate the square of a number."""
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool()
    pool.map(calculate_square, numbers)
    pool.close()
    pool.join()

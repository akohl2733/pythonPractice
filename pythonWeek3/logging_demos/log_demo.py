import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# logging.info("This is an info message")
# logging.warning("Something might be wrong")
# logging.error("Something went wrong")

# --------------------------------------

import pdb

def buggy_function(x):
    result = x * 2
    pdb.set_trace()
    return result + 5

# buggy_function(3)


# ---------------------------------------


logging.basicConfig(level=logging.INFO)

def compute_average(numbers):
    logging.info(f"Received numbers: {numbers}")

    if not numbers:
        logging.warning("Empty list provided - cannot compute average")
        return None
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        logging.exception("Values are not all numerical.")
        return None
    
    total = sum(numbers)
    logging.info(f"Total is {total}")


    try:
        avg = total / len(numbers)
        logging.info(f"Average is {avg}")
        # pdb.set_trace()
        return avg
    except ZeroDivisionError:
        logging.exception("Division by zero occurred.")
        return None

if __name__ == "__main__":
    nums = [10, 20, 30]
    print(f"Average (Valid): {compute_average(nums)}")

    nums2 = ['Andrew']
    print(f"Average (Invalid): {compute_average(nums2)}")
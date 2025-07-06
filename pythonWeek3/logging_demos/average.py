import logging, pdb

logging.basicConfig(level=logging.INFO)

def compute_average(numbers):
    logging.info(f"Received numbers: {numbers}")

    if not numbers:
        logging.warning("Empty list provided - cannot compute average")
        return None
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        logging.error("Values are not all numerical.")
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

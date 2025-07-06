import logging, pdb
from typing import List, Optional

logging.basicConfig(level=logging.INFO)

def compute_average(numbers: List[float]) -> Optional[float]:
    logging.info(f"Received numbers: {numbers}")

    if not numbers:
        logging.warning("Empty list provided - cannot compute average")
        return None
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        logging.error("Values are not all numerical.")
        return None
    
    total: float = sum(numbers)
    logging.info(f"Total is {total}")


    try:
        avg: float = total / len(numbers)
        logging.info(f"Average is {avg}")
        # pdb.set_trace()
        return avg
    except ZeroDivisionError:
        logging.exception("Division by zero occurred.")
        return None

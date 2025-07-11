import logging

def main() -> None:

    logging.basicConfig(
        level=logging.WARNING,  # this is the lowest level that will be printed (DEBUG / INFO / WARNING / ERROR / CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="./logs.py"
    )  

    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

if __name__ == "__main__":
    main()
import re

def email_checker(email: str):
    checker = re.match(r"[\w\.-]+@[\w.-]+\.[\w-]+", email)
    return checker

print("Email:", email_checker('akohl2733@gmail.com'))


def practice(word):
    checker = re.match(r"\w+", word)
    return checker


print("Practice:", practice("Anddrew"))
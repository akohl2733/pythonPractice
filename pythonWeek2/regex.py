import re

# match = re.search(r'[\w.-]+@\w+\.\w+', "My email is and-rew.kohl@gmail.com")
# if match:
#     print("Successful match")
#     print(match.group())
# else:
#     print('Not a match')


# match = re.search(r'([\w.-]+)@(\w+\.\w+)', "My email is and-rew.kohl@gmail.com") # wrap each piece in parenthese to designate them different parts of the groups
# if match:
#     print("Successful match")
#     print(match.group(), match.group(1), match.group(2))
#     print()
# else:
#     print('Not a match')


# match = re.findall(r'[\w.-]+@\w+\.\w+', "My email is and-rew.kohl@gmail.com and my work email is akohl27-33@hhh.com") # findal vs search
# if match:
#     for m in match:
#         print(m)
# else:
#     print('Not a match')


match = re.findall(r'([\w.-]+)@(\w+\.\w+)', "My email is and-rew.kohl@gmail.com and my work email is akohl27-33@hhh.com") # findal vs search
if match:
    for m in match:
        print(m)
        print(m[0], m[1])
        print()
else:
    print('Not a match')
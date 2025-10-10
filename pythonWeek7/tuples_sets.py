def get_user_status(user_id):
    success = True
    data = "User Found"
    return success, data

status_tuple = get_user_status(5)
is_ok, message = get_user_status(5)

# print(is_ok, ": Message:", message)

t = (12345, 67890, 'abcde')
x, y, z = t 
# print(x)
# print(y)
# print(z)


## ---------------------------

ans = {x for x in 'abracadabra' if x not in "abc"}
print(ans)

names = {'andrew', 'blue', 'rich', 'chloe', 'nouse', 'andrew'}
print(names)

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print('a == b:', a == b)
print('a is b:', a is b)

print('a == c:', a == c)
print('a is c:', a is c)

print(a, b, c)
a.append(4)
b.append(9)
c.append(5)
print(a, b, c)

cache = {}

def get_user(user_id):
    if user_id not in cache:
        return ...
    return cache[user_id]

u1 = get_user(7)
u2 = get_user(7)
new = 1

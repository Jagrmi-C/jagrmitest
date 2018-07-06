ar = [1, 5, 2, 1, 4, 0]
c_endpoints = []

for c, r in enumerate(ar):
    c_endpoints += [(c-r, True), (c+r, False)]

c_endpoints.sort(key=lambda x: (x[0], not x[1]))
print(c_endpoints)

i, active_circle = 0, 0
count = 1

for _, is_begining in c_endpoints:

    if is_begining:
        i += active_circle
        active_circle += 1
    else:
        active_circle -= 1
    count += 1
    print(i, count)

print("Answer", i)

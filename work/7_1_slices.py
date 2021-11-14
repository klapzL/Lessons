# Срезы / Slices

t = "0123456789"

print(t[0:6])
# Где 0, - начиная с, где 6, заканчивая перед
print(t[2:7:2])
# С 9 до 2 по 2
print(t[-1:1:-2])

print(t[-1:0:-1])

print(t[:-8:-1])

a = "Hello world!"
print(a[6:10])

print(t[4::-1])
print(t[4:0:-1])

print(t[:2:-2])

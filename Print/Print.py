from pip._vendor.distlib.compat import raw_input

n = int(raw_input())
for x in range(1, n + 1):
    print(x, end="", flush=True)

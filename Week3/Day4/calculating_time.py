import time

start = time.time()
i = 1
for i in range(100):
    print(i)

time.sleep(1)

end = time.time()

print(f"runtime is {end-start}")
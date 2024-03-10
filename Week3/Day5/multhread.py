import threading
import time

# Define a function to simulate a task
def task(thread_name):
    print(f"Thread {thread_name} is starting")
    time.sleep(2)  # Simulate some task execution time
    print(f"Thread {thread_name} is finishing")

if __name__ == "__main__":
    # Create threads
    threads = []
    for i in range(3):
        thread = threading.Thread(target=task, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All threads have finished")

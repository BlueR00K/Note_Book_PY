"""
multithreading_demo.py

A practical demonstration of multithreading in Python, showing:
- Thread creation and management
- Synchronization with Lock
- Race conditions and their prevention
- Downloading multiple web pages concurrently using requests
- Thread-safe counters and timing

This script is designed to be run as a standalone demo for the AdvancedTopics chapter on multithreading and memory access problems.
"""

import threading
import requests
import time

# List of URLs to download
URLS = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.bbc.com",
    "https://www.cnn.com"
]

# Shared counter (demonstrates race condition if not protected)
downloaded_count = 0
count_lock = threading.Lock()

# Shared list to store results (thread-safe with lock)
downloaded_results = []
results_lock = threading.Lock()


def download_url(url, thread_id):
    global downloaded_count
    try:
        print(f"[Thread-{thread_id}] Starting download: {url}")
        response = requests.get(url, timeout=10)
        size = len(response.content)
        print(f"[Thread-{thread_id}] Finished download: {url} ({size} bytes)")
        # Safely increment the counter
        with count_lock:
            downloaded_count += 1
        # Safely append to results
        with results_lock:
            downloaded_results.append((url, size))
    except Exception as e:
        print(f"[Thread-{thread_id}] Error downloading {url}: {e}")


def main():
    threads = []
    start_time = time.time()
    for i, url in enumerate(URLS):
        t = threading.Thread(target=download_url, args=(url, i+1))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print("\nAll downloads complete.")
    print(
        f"Total successful downloads: {downloaded_count} (expected: {len(URLS)})")
    print(f"Total time taken: {end_time - start_time:.2f} seconds\n")
    print("Download results:")
    for url, size in downloaded_results:
        print(f"- {url}: {size} bytes")


if __name__ == "__main__":
    main()

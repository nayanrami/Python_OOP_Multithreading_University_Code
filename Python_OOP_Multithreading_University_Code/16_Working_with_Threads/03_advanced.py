"""ThreadPoolExecutor is a high-level interface over worker threads."""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def io_bound_job(job_id: int) -> tuple[int, int]:
    time.sleep(0.02)
    return job_id, job_id * job_id

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(io_bound_job, i) for i in range(1, 7)]
        results = [future.result() for future in as_completed(futures)]

    # Completion order can differ, so sort only for readable output.
    print(sorted(results))


if __name__ == "__main__":
    main()

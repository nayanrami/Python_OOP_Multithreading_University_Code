"""Thread subclass example."""

import threading
import time

class DownloadSimulation(threading.Thread):
    def __init__(self, file_name: str, chunks: int):
        super().__init__(name=f"Download-{file_name}")
        self.file_name = file_name
        self.chunks = chunks

    def run(self):
        for chunk in range(1, self.chunks + 1):
            time.sleep(0.01)
            print(f"{self.name}: chunk {chunk}/{self.chunks}")


def main():
    jobs = [
        DownloadSimulation("notes.pdf", 3),
        DownloadSimulation("dataset.csv", 4),
    ]
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print("All simulated downloads finished")


if __name__ == "__main__":
    main()

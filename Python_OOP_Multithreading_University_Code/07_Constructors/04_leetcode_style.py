"""LeetCode 359-inspired: Logger Rate Limiter.

Focus: constructor initializes the object's persistent state.
"""

class Logger:
    def __init__(self):
        self.next_allowed_time: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.next_allowed_time.get(message, 0):
            return False
        self.next_allowed_time[message] = timestamp + 10
        return True


def main():
    logger = Logger()
    calls = [(1, "foo"), (2, "bar"), (3, "foo"), (11, "foo"), (12, "bar")]
    for t, msg in calls:
        print(t, msg, logger.shouldPrintMessage(t, msg))


if __name__ == "__main__":
    main()

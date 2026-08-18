"""Supplement: super() augments rather than replaces behavior."""

class Logger:
    def log(self, msg):
        return f"LOG:{msg}"

class TimestampLogger(Logger):
    def log(self, msg):
        return "[time] " + super().log(msg)

if __name__ == "__main__":
    print(TimestampLogger().log("started"))

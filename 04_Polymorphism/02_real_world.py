"""Duck-typed notification polymorphism."""

class EmailNotification:
    def send(self, recipient, message):
        return f"Email to {recipient}: {message}"

class SMSNotification:
    def send(self, recipient, message):
        return f"SMS to {recipient}: {message}"

class ConsoleNotification:
    def send(self, recipient, message):
        return f"Console[{recipient}]: {message}"

def notify(service, recipient, message):
    # No inheritance is required; service only needs a compatible send method.
    print(service.send(recipient, message))


def main():
    services = [EmailNotification(), SMSNotification(), ConsoleNotification()]
    for service in services:
        notify(service, "student", "Exam starts at 10:00")


if __name__ == "__main__":
    main()

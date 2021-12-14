class SubscribeObserver:
    def __init__(self):
        self.subscriptions = []

    def append(self, subscriber):
        if subscriber not in self.subscriptions:
            self.subscriptions.append(subscriber)
        else:
            print("Error: Subscriber Already Exists")

    def delete(self, subscriber):
        if subscriber in self.subscriptions:
            self.subscriptions.remove(subscriber)
        else:
            print("Error: Incorrect Subscriber")

    def notify(self):
        for subscriber in self.subscriptions:
            print(f"Client {subscriber} was notified on the product creation")

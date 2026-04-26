from __future__ import annotations

from queue import Queue


queue: Queue[Request] = Queue()
current_request_no = 0


class Request:
    def __init__(self, description: str, request_no: int | None = None):
        self.description = description
        self.request_no = request_no

    def __str__(self) -> str:
        if self.request_no is None:
            return f"Request: {self.description}"
        return f"Request #{self.request_no}: {self.description}"


def generate_request() -> None:
    global current_request_no

    description = input("Enter request description: ").strip()
    if not description:
        print("Empty description. Request not added.")
        return

    current_request_no += 1
    request = Request(description, request_no=current_request_no)
    queue.put(request)
    print(f"Added {request}")


def process_request() -> None:
    if queue.empty():
        print("No requests to process.")
        return

    request = queue.get()
    print(f"Processed {request}")


def main() -> None:
    while True:
        print("\n1. Generate Request")
        print("2. Process Request")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_request()
        elif choice == "2":
            process_request()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

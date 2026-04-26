from __future__ import annotations

from queue import Queue
import random


queue: Queue[Request] = Queue()
current_request_no = 1


class Request:
    def __init__(self, request_no: int):
        self.request_no = request_no

    def __str__(self) -> str:
        return f"Request #{self.request_no}"


def generate_request() -> None:
    global current_request_no

    request = Request(current_request_no)

    current_request_no += 1

    queue.put(request)
    print(f"Added {request}")


def process_request() -> bool:
    if queue.empty():
        print("No requests to process.")
        return False

    request = queue.get()
    print(f"Processed {request}")
    return True


def main() -> None:
    should_exit = False
    while not should_exit:
        requests_to_generate_count = random.randint(1, 5)
        for _ in range(requests_to_generate_count):
            generate_request()

        queue_size = queue.qsize()
        requests_to_process_count = random.randint(1, queue_size) if queue_size else 0
        for _ in range(requests_to_process_count):
            process_request()

        if queue.qsize() == 0:
            print("The queue is empty.")

        try:
            input("Press Enter to continue or Ctrl+C to exit.")
        except KeyboardInterrupt:
            should_exit = True


if __name__ == "__main__":
    main()

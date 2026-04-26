# goit-algo-hw-02

Homework for Topic 2, **Basic Data Structures**.

This repository contains two independent Python tasks that demonstrate the use of standard data structures:

- `Queue` from the `queue` module for simulating request processing in a service center.
- `deque` from the `collections` module for checking whether a string is a palindrome.

## Project Structure

```text
goit-algo-hw-02/
|-- task1_queue.py
|-- task2_deque.py
`-- README.md
```

## Task 1: Request Queue Simulation

File: `task1_queue.py`

The program simulates a service center request system:

1. Automatically generates new requests with unique numbers.
2. Adds the requests to a queue.
3. Processes requests in FIFO order.
4. Prints a message when the queue is empty.

The implementation uses `Queue` from Python's built-in `queue` module.

Run:

```bash
python task1_queue.py
```

Press `Enter` to continue the simulation or `Ctrl+C` to exit.

## Task 2: Palindrome Checker

File: `task2_deque.py`

The program checks whether a given string is a palindrome:

1. Adds characters to a double-ended queue.
2. Ignores spaces.
3. Ignores letter case.
4. Compares characters from both ends of the queue.

The implementation uses `deque` from Python's built-in `collections` module.

Run:

```bash
python task2_deque.py
```

Enter a string to check whether it is a palindrome. Press `Ctrl+C` to exit.

## Requirements

- Python 3.10 or newer is recommended.
- No external dependencies are required.

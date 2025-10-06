from collections import deque

queue = deque()


def add_event(event):
    queue.append(event)


def process_event():
    if queue:
        return queue.popleft()
    return None


def display_events():
    return list(queue)


def cancel_event(event):
    if event in queue:
        queue.remove(event)


# Main program
add_event("Event1")
add_event("Event2")
add_event("Event3")

print("Pending:", display_events())
print("Processed:", process_event())
cancel_event("Event3")
print("After Cancel:", display_events())

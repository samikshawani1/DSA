queue = [0] * 5

front = -1
rear = -1


# Insert 10
if rear == 4:
    print("Queue Overflow")
else:
    if front == -1:
        front = 0

    rear = rear + 1
    queue[rear] = 10


# Insert 20
if rear == 4:
    print("Queue Overflow")
else:
    rear = rear + 1
    queue[rear] = 20


# Insert 30
if rear == 4:
    print("Queue Overflow")
else:
    rear = rear + 1
    queue[rear] = 30



print("Queue:", end=" ")

for i in range(front, rear + 1):
    print(queue[i], end=" ")

print()

print("Front =", front)
print("Rear =", rear)




if front == -1:
    print("Queue is empty")
else:
    print("Front element:", queue[front])



if front == -1:
    print("Queue Underflow")
else:
    deleted = queue[front]
    print("Deleted:", deleted)

    if front == rear:
        front = -1
        rear = -1
    else:
        front = front + 1




if front == -1:
    print("Queue is empty")
else:
    print("Queue after deletion:", end=" ")

    for i in range(front, rear + 1):
        print(queue[i], end=" ")

    print()

print("Front =", front)
print("Rear =", rear)

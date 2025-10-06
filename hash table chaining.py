size = 10
table = [[] for _ in range(size)]


def insert(key, value):
    index = key % size
    table[index].append((key, value))


def search(key):
    index = key % size
    for k, v in table[index]:
        if k == key:
            return v
    return None


# Main program
insert(21, "Alice")
insert(31, "Bob")
insert(10, "Charlie")

print("Hash Table:", table)
print("Search 31:", search(31))

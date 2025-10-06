#include <iostream>
using namespace std;

const int SIZE = 10;
int hashTable[SIZE];

void init() {
    for (int i = 0; i < SIZE; i++)
        hashTable[i] = -1;
}

int hashFunc(int key) {
    return key % SIZE;
}

void insertKey(int key) {
    int idx = hashFunc(key);
    while (hashTable[idx] != -1) {
        idx = (idx + 1) % SIZE; // Linear probing
    }
    hashTable[idx] = key;
}

bool searchKey(int key) {
    int idx = hashFunc(key);
    int start = idx;
    while (hashTable[idx] != -1) {
        if (hashTable[idx] == key)
            return true;
        idx = (idx + 1) % SIZE;
        if (idx == start)
            break;
    }
    return false;
}

void display() {
    for (int i = 0; i < SIZE; i++) {
        cout << i << ": " << hashTable[i] << endl;
    }
}

int main() {
    init();

    insertKey(21);
    insertKey(31);
    insertKey(41);

    display();

    cout << "Search 31: " << (searchKey(31) ? "Found" : "Not Found") << endl;

    return 0;
}

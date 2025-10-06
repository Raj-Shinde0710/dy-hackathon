undo_stack = []
redo_stack = []
document = ""


def make_change(text):
    global document
    undo_stack.append(document)
    document += text


def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()


def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()


# Main program
make_change("Hello ")
make_change("World")

print("Document:", document)

undo()
print("After Undo:", document)

redo()
print("After Redo:", document)

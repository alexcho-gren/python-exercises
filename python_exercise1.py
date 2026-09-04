x = 1021
y = 5.21
text = "text"
really = True
no = False
none = None

ids = [1, 2, 3]
todo = {"id": 1, "task": "do task"}

todos = [
    {"id": ids[0], "task": "leva"},
    {"id": ids[1], "task": "dö"}
]

print("Saker jag behöver göra:\n")
for todo in todos:
    print(f"{todo["id"]}, {todo["task"]}")
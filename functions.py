FILEPATH = 'todos.txt'
def getTodos(filePath=FILEPATH):
    with open(filePath, 'r') as fileLocal:
        todosLocal = fileLocal.readlines()
    return todosLocal


def writeTodos(todosLocal, filePath=FILEPATH):
    with open(filePath, 'w') as file:
        file.writelines(todosLocal)

if __name__ == "__main__":
    print(getTodos())
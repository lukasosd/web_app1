def file_writter(todos, filepath='todos.txt'):
    with open(filepath, 'w') as myfile:
        myfile.writelines(todos)


def file_reader(filepath='todos.txt'):
    with open(filepath) as myfile:
        todos = myfile.readlines()
    return todos
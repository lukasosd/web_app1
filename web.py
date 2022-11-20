import streamlit as sl
import os
import functions

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

todos = functions.file_reader()
def add_todo():
    todo = sl.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.file_writter(todos)
    sl.session_state['new_todo'] = ''

sl.title('My To-Do App')
sl.subheader('This is my To-Do App')
sl.text('This is the list of the things that I need to do:')

for todo in todos:
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.file_writter(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

sl.text_input(label='', placeholder='Add new todo...', on_change=add_todo, key='new_todo')
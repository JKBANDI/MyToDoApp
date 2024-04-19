import streamlit as sl
import functions


todos = functions.get_todos()

def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)



sl.title('My todo app')
sl.subheader('this is my todo app')
sl.text('this app is to increase productivity.')

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()


sl.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")


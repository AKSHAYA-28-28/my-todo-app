import streamlit as st
import functions

def add_todos():

    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()
st.title("my todo app")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")
st.checkbox("buy grocery")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]

st.text_input(label="", placeholder="enter a new todo....",on_change=add_todos, key='new_todo')

st.session_state

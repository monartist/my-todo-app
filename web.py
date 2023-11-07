import streamlit as st
import functions

todos = functions.getTodos()
def addTodo():
    todo = st.session_state['newTodo'] + '\n'
    todos.append(todo)
    functions.writeTodos(todos)

st.title('My Todo App')
st.subheader('This is my todo app.')
st.text('This is the list of my todos...')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="New to do:", placeholder='Add new todo...',
              key='newTodo', on_change=addTodo)

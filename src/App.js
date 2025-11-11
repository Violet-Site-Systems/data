import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [todos, setTodos] = useState(() => {
    const saved = localStorage.getItem("todos");
    return saved ? JSON.parse(saved) : [];
  });
  const [input, setInput] = useState("");

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  const addTodo = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setTodos([
      ...todos,
      { text: input.trim(), completed: false, id: Date.now() }
    ]);
    setInput("");
  };

  const toggleComplete = (id) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id
          ? { ...todo, completed: !todo.completed }
          : todo
      )
    );
  };

  const removeTodo = (id) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };

  return (
    <div className="container">
      <h1>📝 To-Do List</h1>
      <form onSubmit={addTodo} className="todo-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Add a new task..."
          className="todo-input"
        />
        <button type="submit" className="todo-add-btn">Add</button>
      </form>
      <ul className="todo-list">
        {todos.length === 0 ? (
          <li className="empty-message">No tasks yet!</li>
        ) : (
          todos.map((todo) => (
            <li key={todo.id} className={todo.completed ? "completed" : ""}>
              <label>
                <input
                  type="checkbox"
                  checked={todo.completed}
                  onChange={() => toggleComplete(todo.id)}
                />
                <span>{todo.text}</span>
              </label>
              <button className="delete-btn" onClick={() => removeTodo(todo.id)}>
                ❌
              </button>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}

export default App;

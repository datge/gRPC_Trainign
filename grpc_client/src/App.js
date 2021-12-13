import logo from './logo.svg';
import './App.css';
import {AddTodoRequest} from './proto/todo_pb';
import { TodoServiceClient } from './proto/todo_grpc_pb';

function App() {
  const client = new TodoServiceClient('localhost:50051', );

  const addTodoRequest = new AddTodoRequest();
  addTodoRequest.setTask('My new task');
  addTodoRequest.setStatus('complete');

  client.addTodo(addTodoRequest, (err, response) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(response);
  });
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

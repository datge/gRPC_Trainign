import sqlite3
import grpc
import concurrent
from concurrent import futures
import proto.todo_pb2_grpc as todo_pb2_grpc
import proto.todo_pb2 as todo_pb2

class TodoServiceServicer(todo_pb2_grpc.TodoServiceServicer):
  def GetTodo(self, request, context):
    print("We got something!")
    con = sqlite3.connect('todos.db')
    cur = con.cursor();
    response = todo_pb2.GetTodoResponse();
    for row in cur.execute(f"SELECT * FROM todos WHERE id = {request.id}"):    
      response.id = row[0]
      response.task = row[1]
      response.status = row[2]
    return response
  
  def AddTodo(self, request, context):
    print("We got something!", request)
    con = sqlite3.connect('todos.db')
    cur = con.cursor();
    cur.execute(f"INSERT INTO todos (task, status) VALUES ('{request.task}', '{request.status}')")
    con.commit()
    con.close()
    response = todo_pb2.AddTodoResponse();
    response.task = request.task
    response.status = request.status
    return response
  
  def UpdateTodo(self, request, context):
    print("We got something!", request)
    con = sqlite3.connect('todos.db')
    cur = con.cursor();
    cur.execute(f"UPDATE todos SET task = '{request.task}', status = '{request.status}' WHERE id = {request.id}")
    con.commit()
    con.close()
    response = todo_pb2.UpdateTodoResponse();
    response.task = request.task
    response.status = request.status
    return response
  
  def DeleteTodo(self, request, context):
    print("We got something!", request)
    con = sqlite3.connect('todos.db')
    cur = con.cursor();
    cur.execute(f"DELETE FROM todos WHERE id = {request.id}")
    con.commit() 
    con.close()
    response = todo_pb2.DeleteTodoResponse();
    response.id = request.id
    return response
    
def main():
  # print("Hello World!")
  # cur = con.cursor()
  # # cur.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task text, status text)")
  # # cur.execute("INSERT INTO todos (task, status) VALUES ('Learn SQLite', 'incomplete')")
  # # con.commit()
  # for row in cur.execute("SELECT * FROM todos"):
  #   print(row)
  # con.close()
  
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoServiceServicer(), server)
  print('Server Started. Listening on port 50051')
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()
  
  
  
  
if __name__ == '__main__':
  main()

# import grpc
# import concurrent
# from concurrent import futures

# import ice_cream_pb2
# import ice_cream_pb2_grpc

# class IceCreamServicer(ice_cream_pb2_grpc.IceCreamServicer):
#   def OrderIceCream(self, request, context):
#     print('we got something!!')
#     response = ice_cream_pb2.IceCreamResponse()
#     response.message = f"here is your {request.scoops} scoop {request.flavor} ice cream!"
#     return response

# def main():
#   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#   ice_cream_pb2_grpc.add_IceCreamServicer_to_server(IceCreamServicer(), server)
#   print('Server Started. Listening on port 50051')
#   server.add_insecure_port('[::]:50051')
#   server.start()
#   server.wait_for_termination()

# main()

// GENERATED CODE -- DO NOT EDIT!

var grpc = require('@grpc/grpc-js');
var todo_pb = require('./todo_pb.js');

function serialize_AddTodoRequest(arg) {
  if (!(arg instanceof todo_pb.AddTodoRequest)) {
    throw new Error('Expected argument of type AddTodoRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_AddTodoRequest(buffer_arg) {
  return todo_pb.AddTodoRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_AddTodoResponse(arg) {
  if (!(arg instanceof todo_pb.AddTodoResponse)) {
    throw new Error('Expected argument of type AddTodoResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_AddTodoResponse(buffer_arg) {
  return todo_pb.AddTodoResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_DeleteTodoRequest(arg) {
  if (!(arg instanceof todo_pb.DeleteTodoRequest)) {
    throw new Error('Expected argument of type DeleteTodoRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_DeleteTodoRequest(buffer_arg) {
  return todo_pb.DeleteTodoRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_DeleteTodoResponse(arg) {
  if (!(arg instanceof todo_pb.DeleteTodoResponse)) {
    throw new Error('Expected argument of type DeleteTodoResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_DeleteTodoResponse(buffer_arg) {
  return todo_pb.DeleteTodoResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetTodoRequest(arg) {
  if (!(arg instanceof todo_pb.GetTodoRequest)) {
    throw new Error('Expected argument of type GetTodoRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetTodoRequest(buffer_arg) {
  return todo_pb.GetTodoRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GetTodoResponse(arg) {
  if (!(arg instanceof todo_pb.GetTodoResponse)) {
    throw new Error('Expected argument of type GetTodoResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GetTodoResponse(buffer_arg) {
  return todo_pb.GetTodoResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_UpdateTodoRequest(arg) {
  if (!(arg instanceof todo_pb.UpdateTodoRequest)) {
    throw new Error('Expected argument of type UpdateTodoRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_UpdateTodoRequest(buffer_arg) {
  return todo_pb.UpdateTodoRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_UpdateTodoResponse(arg) {
  if (!(arg instanceof todo_pb.UpdateTodoResponse)) {
    throw new Error('Expected argument of type UpdateTodoResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_UpdateTodoResponse(buffer_arg) {
  return todo_pb.UpdateTodoResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var TodoServiceService = exports.TodoServiceService = {
  getTodo: {
    path: '/TodoService/GetTodo',
    requestStream: false,
    responseStream: false,
    requestType: todo_pb.GetTodoRequest,
    responseType: todo_pb.GetTodoResponse,
    requestSerialize: serialize_GetTodoRequest,
    requestDeserialize: deserialize_GetTodoRequest,
    responseSerialize: serialize_GetTodoResponse,
    responseDeserialize: deserialize_GetTodoResponse,
  },
  addTodo: {
    path: '/TodoService/AddTodo',
    requestStream: false,
    responseStream: false,
    requestType: todo_pb.AddTodoRequest,
    responseType: todo_pb.AddTodoResponse,
    requestSerialize: serialize_AddTodoRequest,
    requestDeserialize: deserialize_AddTodoRequest,
    responseSerialize: serialize_AddTodoResponse,
    responseDeserialize: deserialize_AddTodoResponse,
  },
  updateTodo: {
    path: '/TodoService/UpdateTodo',
    requestStream: false,
    responseStream: false,
    requestType: todo_pb.UpdateTodoRequest,
    responseType: todo_pb.UpdateTodoResponse,
    requestSerialize: serialize_UpdateTodoRequest,
    requestDeserialize: deserialize_UpdateTodoRequest,
    responseSerialize: serialize_UpdateTodoResponse,
    responseDeserialize: deserialize_UpdateTodoResponse,
  },
  deleteTodo: {
    path: '/TodoService/DeleteTodo',
    requestStream: false,
    responseStream: false,
    requestType: todo_pb.DeleteTodoRequest,
    responseType: todo_pb.DeleteTodoResponse,
    requestSerialize: serialize_DeleteTodoRequest,
    requestDeserialize: deserialize_DeleteTodoRequest,
    responseSerialize: serialize_DeleteTodoResponse,
    responseDeserialize: deserialize_DeleteTodoResponse,
  },
};

exports.TodoServiceClient = grpc.makeGenericClientConstructor(TodoServiceService);

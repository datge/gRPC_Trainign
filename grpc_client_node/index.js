const grpc = require('@grpc/grpc-js');
// const grpc = require('grpc');
const messages = require('./proto/todo_pb');
const services = require('./proto/todo_grpc_pb');

function main() {

  const grpcCredentials = grpc.credentials.createInsecure();
  //create grpc client fro TodoServiceClient
  const client = new services.TodoServiceClient(
  'localhost:50051', grpcCredentials);

  var Args = process.argv.slice(2);
  
  switch (Args[0]) {

    case 'get':
      const GetTodoRequest = new messages.GetTodoRequest();
      GetTodoRequest.setId(2);
      client.getTodo(GetTodoRequest, function (err, response) {
        if (err) {
          console.log('this thing broke!', err);
        } else {
          console.log('response from python:', response);
        }
      })
      break;

    case 'add':
      const AddTodoRequest = new messages.AddTodoRequest();
      AddTodoRequest.setTask('Learn');
      AddTodoRequest.setStatus('running');

      client.addTodo(AddTodoRequest, function (err, response) {
        if (err) {
          console.log('this thing broke!', err);
        } else {
          console.log('response from python:', response);
        }
      })
      break;

    case 'update':
      const UpdateTodoRequest = new messages.UpdateTodoRequest();
      UpdateTodoRequest.setId(3);
      UpdateTodoRequest.setTask('Learn2');
      UpdateTodoRequest.setStatus('running2');
    
      client.updateTodo(UpdateTodoRequest, function (err, response) {
        if (err) {
          console.log('this thing broke!', err);
        } else {
          console.log('response from python:', response);
        }
      })
      break;

    case 'delete':
      const DeleteTodoRequest = new messages.DeleteTodoRequest();
      DeleteTodoRequest.setId(3);

      client.deleteTodo(DeleteTodoRequest, function (err, response) {
        if (err) {
          console.log('this thing broke!', err);
        } else {
          console.log('response from python:', response);
        }
      })
      break;
  
    default:
      break;
  }
}

main();


// const grpc = require('grpc');
// const messages = require('./iceProto/ice_cream_pb');
// const services = require('./iceProto/ice_cream_grpc_pb');

// function main() {
//   const client = new services.IceCreamClient(
//     'localhost:50051', grpc.credentials.createInsecure()
//   );

//   const iceCreamRequest = new messages.IceCreamRequest();
//   iceCreamRequest.setScoops(3);
//   iceCreamRequest.setFlavor('strawberry');

//   client.orderIceCream(iceCreamRequest, function (err, response) {
//     if (err) {
//       console.log('this thing broke!', err);
//     } else {
//       console.log('response from python:', response.getMessage());
//     }
//   })
// }

// main();

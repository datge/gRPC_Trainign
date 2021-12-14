# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntodo.proto\".\n\x0e\x41\x64\x64TodoRequest\x12\x0c\n\x04task\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"/\n\x0f\x41\x64\x64TodoResponse\x12\x0c\n\x04task\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x1c\n\x0eGetTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\";\n\x0fGetTodoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"0\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"/\n\x0fGetTodosRequest\x12\x0c\n\x04task\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"(\n\x10GetTodosResponse\x12\x14\n\x05todos\x18\x01 \x03(\x0b\x32\x05.Todo\"=\n\x11UpdateTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\">\n\x12UpdateTodoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"\x1f\n\x11\x44\x65leteTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\" \n\x12\x44\x65leteTodoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x88\x02\n\x0bTodoService\x12,\n\x07GetTodo\x12\x0f.GetTodoRequest\x1a\x10.GetTodoResponse\x12,\n\x07\x41\x64\x64Todo\x12\x0f.AddTodoRequest\x1a\x10.AddTodoResponse\x12\x35\n\nUpdateTodo\x12\x12.UpdateTodoRequest\x1a\x13.UpdateTodoResponse\x12\x35\n\nDeleteTodo\x12\x12.DeleteTodoRequest\x1a\x13.DeleteTodoResponse\x12/\n\x08GetTodos\x12\x10.GetTodosRequest\x1a\x11.GetTodosResponseb\x06proto3'
)




_ADDTODOREQUEST = _descriptor.Descriptor(
  name='AddTodoRequest',
  full_name='AddTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='AddTodoRequest.task', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='AddTodoRequest.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=60,
)


_ADDTODORESPONSE = _descriptor.Descriptor(
  name='AddTodoResponse',
  full_name='AddTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='AddTodoResponse.task', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='AddTodoResponse.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=109,
)


_GETTODOREQUEST = _descriptor.Descriptor(
  name='GetTodoRequest',
  full_name='GetTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetTodoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=139,
)


_GETTODORESPONSE = _descriptor.Descriptor(
  name='GetTodoResponse',
  full_name='GetTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetTodoResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='GetTodoResponse.task', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='GetTodoResponse.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=200,
)


_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Todo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='Todo.task', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='Todo.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=250,
)


_GETTODOSREQUEST = _descriptor.Descriptor(
  name='GetTodosRequest',
  full_name='GetTodosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='GetTodosRequest.task', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='GetTodosRequest.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=299,
)


_GETTODOSRESPONSE = _descriptor.Descriptor(
  name='GetTodosResponse',
  full_name='GetTodosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='todos', full_name='GetTodosResponse.todos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=341,
)


_UPDATETODOREQUEST = _descriptor.Descriptor(
  name='UpdateTodoRequest',
  full_name='UpdateTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateTodoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='UpdateTodoRequest.task', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='UpdateTodoRequest.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=404,
)


_UPDATETODORESPONSE = _descriptor.Descriptor(
  name='UpdateTodoResponse',
  full_name='UpdateTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateTodoResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='UpdateTodoResponse.task', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='UpdateTodoResponse.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=468,
)


_DELETETODOREQUEST = _descriptor.Descriptor(
  name='DeleteTodoRequest',
  full_name='DeleteTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeleteTodoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=501,
)


_DELETETODORESPONSE = _descriptor.Descriptor(
  name='DeleteTodoResponse',
  full_name='DeleteTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeleteTodoResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=535,
)

_GETTODOSRESPONSE.fields_by_name['todos'].message_type = _TODO
DESCRIPTOR.message_types_by_name['AddTodoRequest'] = _ADDTODOREQUEST
DESCRIPTOR.message_types_by_name['AddTodoResponse'] = _ADDTODORESPONSE
DESCRIPTOR.message_types_by_name['GetTodoRequest'] = _GETTODOREQUEST
DESCRIPTOR.message_types_by_name['GetTodoResponse'] = _GETTODORESPONSE
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['GetTodosRequest'] = _GETTODOSREQUEST
DESCRIPTOR.message_types_by_name['GetTodosResponse'] = _GETTODOSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateTodoRequest'] = _UPDATETODOREQUEST
DESCRIPTOR.message_types_by_name['UpdateTodoResponse'] = _UPDATETODORESPONSE
DESCRIPTOR.message_types_by_name['DeleteTodoRequest'] = _DELETETODOREQUEST
DESCRIPTOR.message_types_by_name['DeleteTodoResponse'] = _DELETETODORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddTodoRequest = _reflection.GeneratedProtocolMessageType('AddTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDTODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:AddTodoRequest)
  })
_sym_db.RegisterMessage(AddTodoRequest)

AddTodoResponse = _reflection.GeneratedProtocolMessageType('AddTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDTODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:AddTodoResponse)
  })
_sym_db.RegisterMessage(AddTodoResponse)

GetTodoRequest = _reflection.GeneratedProtocolMessageType('GetTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:GetTodoRequest)
  })
_sym_db.RegisterMessage(GetTodoRequest)

GetTodoResponse = _reflection.GeneratedProtocolMessageType('GetTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:GetTodoResponse)
  })
_sym_db.RegisterMessage(GetTodoResponse)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), {
  'DESCRIPTOR' : _TODO,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:Todo)
  })
_sym_db.RegisterMessage(Todo)

GetTodosRequest = _reflection.GeneratedProtocolMessageType('GetTodosRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTODOSREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:GetTodosRequest)
  })
_sym_db.RegisterMessage(GetTodosRequest)

GetTodosResponse = _reflection.GeneratedProtocolMessageType('GetTodosResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTODOSRESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:GetTodosResponse)
  })
_sym_db.RegisterMessage(GetTodosResponse)

UpdateTodoRequest = _reflection.GeneratedProtocolMessageType('UpdateTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:UpdateTodoRequest)
  })
_sym_db.RegisterMessage(UpdateTodoRequest)

UpdateTodoResponse = _reflection.GeneratedProtocolMessageType('UpdateTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:UpdateTodoResponse)
  })
_sym_db.RegisterMessage(UpdateTodoResponse)

DeleteTodoRequest = _reflection.GeneratedProtocolMessageType('DeleteTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:DeleteTodoRequest)
  })
_sym_db.RegisterMessage(DeleteTodoRequest)

DeleteTodoResponse = _reflection.GeneratedProtocolMessageType('DeleteTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETETODORESPONSE,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:DeleteTodoResponse)
  })
_sym_db.RegisterMessage(DeleteTodoResponse)



_TODOSERVICE = _descriptor.ServiceDescriptor(
  name='TodoService',
  full_name='TodoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=538,
  serialized_end=802,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTodo',
    full_name='TodoService.GetTodo',
    index=0,
    containing_service=None,
    input_type=_GETTODOREQUEST,
    output_type=_GETTODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddTodo',
    full_name='TodoService.AddTodo',
    index=1,
    containing_service=None,
    input_type=_ADDTODOREQUEST,
    output_type=_ADDTODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTodo',
    full_name='TodoService.UpdateTodo',
    index=2,
    containing_service=None,
    input_type=_UPDATETODOREQUEST,
    output_type=_UPDATETODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTodo',
    full_name='TodoService.DeleteTodo',
    index=3,
    containing_service=None,
    input_type=_DELETETODOREQUEST,
    output_type=_DELETETODORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTodos',
    full_name='TodoService.GetTodos',
    index=4,
    containing_service=None,
    input_type=_GETTODOSREQUEST,
    output_type=_GETTODOSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOSERVICE)

DESCRIPTOR.services_by_name['TodoService'] = _TODOSERVICE

# @@protoc_insertion_point(module_scope)

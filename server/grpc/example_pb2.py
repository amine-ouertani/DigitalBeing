# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\"^\n\x07Request\x12$\n\x06kwargs\x18\x01 \x03(\x0b\x32\x14.Request.KwargsEntry\x1a-\n\x0bKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"f\n\x08Response\x12)\n\x08response\x18\x01 \x03(\x0b\x32\x17.Response.ResponseEntry\x1a/\n\rResponseEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xd9\x02\n\x05\x41gent\x12)\n\x10InitializeAgents\x12\x08.Request\x1a\t.Response\"\x00\x12&\n\rHandleMessage\x12\x08.Request\x1a\t.Response\"\x00\x12(\n\x0fInvokeSoloAgent\x12\x08.Request\x1a\t.Response\"\x00\x12\"\n\tGetAgents\x12\x08.Request\x1a\t.Response\"\x00\x12\'\n\x0eSetAgentFields\x12\x08.Request\x1a\t.Response\"\x00\x12+\n\x12HandleSlashCommand\x12\x08.Request\x1a\t.Response\"\x00\x12)\n\x10HandleUserUpdate\x12\x08.Request\x1a\t.Response\"\x00\x12.\n\x15HandleMessageReaction\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3'
)




_REQUEST_KWARGSENTRY = _descriptor.Descriptor(
  name='KwargsEntry',
  full_name='Request.KwargsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Request.KwargsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Request.KwargsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=111,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='Request.kwargs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_KWARGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=111,
)


_RESPONSE_RESPONSEENTRY = _descriptor.Descriptor(
  name='ResponseEntry',
  full_name='Response.ResponseEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Response.ResponseEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Response.ResponseEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=215,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='Response.response', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_RESPONSEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=215,
)

_REQUEST_KWARGSENTRY.containing_type = _REQUEST
_REQUEST.fields_by_name['kwargs'].message_type = _REQUEST_KWARGSENTRY
_RESPONSE_RESPONSEENTRY.containing_type = _RESPONSE
_RESPONSE.fields_by_name['response'].message_type = _RESPONSE_RESPONSEENTRY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'KwargsEntry' : _reflection.GeneratedProtocolMessageType('KwargsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_KWARGSENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:Request.KwargsEntry)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.KwargsEntry)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {

  'ResponseEntry' : _reflection.GeneratedProtocolMessageType('ResponseEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_RESPONSEENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:Response.ResponseEntry)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.ResponseEntry)


_REQUEST_KWARGSENTRY._options = None
_RESPONSE_RESPONSEENTRY._options = None

_AGENT = _descriptor.ServiceDescriptor(
  name='Agent',
  full_name='Agent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=218,
  serialized_end=563,
  methods=[
  _descriptor.MethodDescriptor(
    name='InitializeAgents',
    full_name='Agent.InitializeAgents',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleMessage',
    full_name='Agent.HandleMessage',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InvokeSoloAgent',
    full_name='Agent.InvokeSoloAgent',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAgents',
    full_name='Agent.GetAgents',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetAgentFields',
    full_name='Agent.SetAgentFields',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleSlashCommand',
    full_name='Agent.HandleSlashCommand',
    index=5,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleUserUpdate',
    full_name='Agent.HandleUserUpdate',
    index=6,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleMessageReaction',
    full_name='Agent.HandleMessageReaction',
    index=7,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENT)

DESCRIPTOR.services_by_name['Agent'] = _AGENT

# @@protoc_insertion_point(module_scope)

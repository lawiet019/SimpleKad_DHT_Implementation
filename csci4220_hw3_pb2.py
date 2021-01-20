


# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: csci4220_hw3.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='csci4220_hw3.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x63sci4220_hw3.proto\"1\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"@\n\x08NodeList\x12\x1e\n\x0fresponding_node\x18\x01 \x01(\x0b\x32\x05.Node\x12\x14\n\x05nodes\x18\x02 \x03(\x0b\x32\x05.Node\"+\n\x05IDKey\x12\x13\n\x04node\x18\x01 \x01(\x0b\x32\x05.Node\x12\r\n\x05idkey\x18\x02 \x01(\r\";\n\x08KeyValue\x12\x13\n\x04node\x18\x01 \x01(\x0b\x32\x05.Node\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\"o\n\x0fKV_Node_Wrapper\x12\x1e\n\x0fresponding_node\x18\x01 \x01(\x0b\x32\x05.Node\x12\x0f\n\x07mode_kv\x18\x02 \x01(\x08\x12\x15\n\x02kv\x18\x03 \x01(\x0b\x32\t.KeyValue\x12\x14\n\x05nodes\x18\x04 \x03(\x0b\x32\x05.Node2\x8b\x01\n\x07KadImpl\x12\x1f\n\x08\x46indNode\x12\x06.IDKey\x1a\t.NodeList\"\x00\x12\'\n\tFindValue\x12\x06.IDKey\x1a\x10.KV_Node_Wrapper\"\x00\x12\x1c\n\x05Store\x12\t.KeyValue\x1a\x06.IDKey\"\x00\x12\x18\n\x04Quit\x12\x06.IDKey\x1a\x06.IDKey\"\x00\x62\x06proto3'
)




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Node.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='Node.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='Node.address', index=2,
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
  serialized_start=22,
  serialized_end=71,
)


_NODELIST = _descriptor.Descriptor(
  name='NodeList',
  full_name='NodeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='responding_node', full_name='NodeList.responding_node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='NodeList.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=73,
  serialized_end=137,
)


_IDKEY = _descriptor.Descriptor(
  name='IDKey',
  full_name='IDKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='IDKey.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idkey', full_name='IDKey.idkey', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=139,
  serialized_end=182,
)


_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='KeyValue.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='KeyValue.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='KeyValue.value', index=2,
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
  serialized_start=184,
  serialized_end=243,
)


_KV_NODE_WRAPPER = _descriptor.Descriptor(
  name='KV_Node_Wrapper',
  full_name='KV_Node_Wrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='responding_node', full_name='KV_Node_Wrapper.responding_node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode_kv', full_name='KV_Node_Wrapper.mode_kv', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kv', full_name='KV_Node_Wrapper.kv', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='KV_Node_Wrapper.nodes', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=245,
  serialized_end=356,
)

_NODELIST.fields_by_name['responding_node'].message_type = _NODE
_NODELIST.fields_by_name['nodes'].message_type = _NODE
_IDKEY.fields_by_name['node'].message_type = _NODE
_KEYVALUE.fields_by_name['node'].message_type = _NODE
_KV_NODE_WRAPPER.fields_by_name['responding_node'].message_type = _NODE
_KV_NODE_WRAPPER.fields_by_name['kv'].message_type = _KEYVALUE
_KV_NODE_WRAPPER.fields_by_name['nodes'].message_type = _NODE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['NodeList'] = _NODELIST
DESCRIPTOR.message_types_by_name['IDKey'] = _IDKEY
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['KV_Node_Wrapper'] = _KV_NODE_WRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'csci4220_hw3_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  })
_sym_db.RegisterMessage(Node)

NodeList = _reflection.GeneratedProtocolMessageType('NodeList', (_message.Message,), {
  'DESCRIPTOR' : _NODELIST,
  '__module__' : 'csci4220_hw3_pb2'
  # @@protoc_insertion_point(class_scope:NodeList)
  })
_sym_db.RegisterMessage(NodeList)

IDKey = _reflection.GeneratedProtocolMessageType('IDKey', (_message.Message,), {
  'DESCRIPTOR' : _IDKEY,
  '__module__' : 'csci4220_hw3_pb2'
  # @@protoc_insertion_point(class_scope:IDKey)
  })
_sym_db.RegisterMessage(IDKey)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), {
  'DESCRIPTOR' : _KEYVALUE,
  '__module__' : 'csci4220_hw3_pb2'
  # @@protoc_insertion_point(class_scope:KeyValue)
  })
_sym_db.RegisterMessage(KeyValue)

KV_Node_Wrapper = _reflection.GeneratedProtocolMessageType('KV_Node_Wrapper', (_message.Message,), {
  'DESCRIPTOR' : _KV_NODE_WRAPPER,
  '__module__' : 'csci4220_hw3_pb2'
  # @@protoc_insertion_point(class_scope:KV_Node_Wrapper)
  })
_sym_db.RegisterMessage(KV_Node_Wrapper)



_KADIMPL = _descriptor.ServiceDescriptor(
  name='KadImpl',
  full_name='KadImpl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=359,
  serialized_end=498,
  methods=[
  _descriptor.MethodDescriptor(
    name='FindNode',
    full_name='KadImpl.FindNode',
    index=0,
    containing_service=None,
    input_type=_IDKEY,
    output_type=_NODELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FindValue',
    full_name='KadImpl.FindValue',
    index=1,
    containing_service=None,
    input_type=_IDKEY,
    output_type=_KV_NODE_WRAPPER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Store',
    full_name='KadImpl.Store',
    index=2,
    containing_service=None,
    input_type=_KEYVALUE,
    output_type=_IDKEY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Quit',
    full_name='KadImpl.Quit',
    index=3,
    containing_service=None,
    input_type=_IDKEY,
    output_type=_IDKEY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KADIMPL)

DESCRIPTOR.services_by_name['KadImpl'] = _KADIMPL

# @@protoc_insertion_point(module_scope)

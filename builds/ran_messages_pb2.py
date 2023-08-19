# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ran_messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ran_messages.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x12ran_messages.proto\"\x89\x01\n\x13RAN_param_map_entry\x12\x1b\n\x03key\x18\x01 \x02(\x0e\x32\x0e.RAN_parameter\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x1d\n\x07ue_list\x18\x04 \x01(\x0b\x32\n.ue_list_mH\x00\x42\x07\n\x05value\"?\n\x16RAN_indication_request\x12%\n\rtarget_params\x18\x01 \x03(\x0e\x32\x0e.RAN_parameter\"_\n\x17RAN_indication_response\x12\'\n\tparam_map\x18\x01 \x03(\x0b\x32\x14.RAN_param_map_entry\x12\x1b\n\x07ue_info\x18\x02 \x03(\x0b\x32\n.ue_info_m\"E\n\x13RAN_control_request\x12.\n\x10target_param_map\x18\x01 \x03(\x0b\x32\x14.RAN_param_map_entry\"\'\n\x08RAN_rsrp\x12\x1b\n\x07ue_info\x18\x01 \x03(\x0b\x32\n.ue_info_m\")\n\nRAN_ber_up\x12\x1b\n\x07ue_info\x18\x01 \x03(\x0b\x32\n.ue_info_m\"+\n\x0cRAN_ber_down\x12\x1b\n\x07ue_info\x18\x01 \x03(\x0b\x32\n.ue_info_m\")\n\nRAN_mcs_up\x12\x1b\n\x07ue_info\x18\x01 \x03(\x0b\x32\n.ue_info_m\"+\n\x0cRAN_mcs_down\x12\x1b\n\x07ue_info\x18\x01 \x03(\x0b\x32\n.ue_info_m\"\x9d\x03\n\x0bRAN_message\x12#\n\x08msg_type\x18\x01 \x02(\x0e\x32\x11.RAN_message_type\x12\x39\n\x16ran_indication_request\x18\x02 \x01(\x0b\x32\x17.RAN_indication_requestH\x00\x12;\n\x17ran_indication_response\x18\x03 \x01(\x0b\x32\x18.RAN_indication_responseH\x00\x12\x33\n\x13ran_control_request\x18\x04 \x01(\x0b\x32\x14.RAN_control_requestH\x00\x12\x1d\n\x08ran_rsrp\x18\x05 \x01(\x0b\x32\t.RAN_rsrpH\x00\x12!\n\nran_ber_up\x18\x06 \x01(\x0b\x32\x0b.RAN_ber_upH\x00\x12%\n\x0cran_ber_down\x18\x07 \x01(\x0b\x32\r.RAN_ber_downH\x00\x12!\n\nran_mcs_up\x18\x08 \x01(\x0b\x32\x0b.RAN_mcs_upH\x00\x12%\n\x0cran_mcs_down\x18\t \x01(\x0b\x32\r.RAN_mcs_downH\x00\x42\t\n\x07payload\"z\n\tue_info_m\x12\x0c\n\x04rnti\x18\x01 \x02(\x05\x12\x0f\n\x07ue_rsrp\x18\x02 \x01(\x02\x12\x11\n\tue_ber_up\x18\x03 \x01(\x02\x12\x13\n\x0bue_ber_down\x18\x04 \x01(\x02\x12\x11\n\tue_mcs_up\x18\x05 \x01(\x02\x12\x13\n\x0bue_mcs_down\x18\x06 \x01(\x02\"W\n\tue_list_m\x12\x15\n\rconnected_ues\x18\x01 \x02(\x05\x12\x16\n\x0e\x61llocated_prbs\x18\x03 \x02(\x05\x12\x1b\n\x07ue_info\x18\x02 \x03(\x0b\x32\n.ue_info_m*\xa0\x01\n\x10RAN_message_type\x12\x10\n\x0cSUBSCRIPTION\x10\x01\x12\x16\n\x12INDICATION_REQUEST\x10\x02\x12\x17\n\x13INDICATION_RESPONSE\x10\x03\x12\x0b\n\x07\x43ONTROL\x10\x04\x12\x08\n\x04RSRP\x10\x05\x12\n\n\x06\x42\x45R_UP\x10\x06\x12\x0c\n\x08\x42\x45R_DOWN\x10\x07\x12\n\n\x06MCS_UP\x10\x08\x12\x0c\n\x08MCS_DOWN\x10\t*(\n\rRAN_parameter\x12\n\n\x06GNB_ID\x10\x01\x12\x0b\n\x07UE_LIST\x10\x03')
)

_RAN_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='RAN_message_type',
  full_name='RAN_message_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIPTION', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDICATION_REQUEST', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDICATION_RESPONSE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RSRP', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BER_UP', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BER_DOWN', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MCS_UP', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MCS_DOWN', index=8, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1242,
  serialized_end=1402,
)
_sym_db.RegisterEnumDescriptor(_RAN_MESSAGE_TYPE)

RAN_message_type = enum_type_wrapper.EnumTypeWrapper(_RAN_MESSAGE_TYPE)
_RAN_PARAMETER = _descriptor.EnumDescriptor(
  name='RAN_parameter',
  full_name='RAN_parameter',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GNB_ID', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UE_LIST', index=1, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1404,
  serialized_end=1444,
)
_sym_db.RegisterEnumDescriptor(_RAN_PARAMETER)

RAN_parameter = enum_type_wrapper.EnumTypeWrapper(_RAN_PARAMETER)
SUBSCRIPTION = 1
INDICATION_REQUEST = 2
INDICATION_RESPONSE = 3
CONTROL = 4
RSRP = 5
BER_UP = 6
BER_DOWN = 7
MCS_UP = 8
MCS_DOWN = 9
GNB_ID = 1
UE_LIST = 3



_RAN_PARAM_MAP_ENTRY = _descriptor.Descriptor(
  name='RAN_param_map_entry',
  full_name='RAN_param_map_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='RAN_param_map_entry.key', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='RAN_param_map_entry.int64_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='RAN_param_map_entry.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_list', full_name='RAN_param_map_entry.ue_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='RAN_param_map_entry.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=23,
  serialized_end=160,
)


_RAN_INDICATION_REQUEST = _descriptor.Descriptor(
  name='RAN_indication_request',
  full_name='RAN_indication_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_params', full_name='RAN_indication_request.target_params', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=225,
)


_RAN_INDICATION_RESPONSE = _descriptor.Descriptor(
  name='RAN_indication_response',
  full_name='RAN_indication_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_map', full_name='RAN_indication_response.param_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_info', full_name='RAN_indication_response.ue_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=322,
)


_RAN_CONTROL_REQUEST = _descriptor.Descriptor(
  name='RAN_control_request',
  full_name='RAN_control_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_param_map', full_name='RAN_control_request.target_param_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=393,
)


_RAN_RSRP = _descriptor.Descriptor(
  name='RAN_rsrp',
  full_name='RAN_rsrp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ue_info', full_name='RAN_rsrp.ue_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=434,
)


_RAN_BER_UP = _descriptor.Descriptor(
  name='RAN_ber_up',
  full_name='RAN_ber_up',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ue_info', full_name='RAN_ber_up.ue_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=477,
)


_RAN_BER_DOWN = _descriptor.Descriptor(
  name='RAN_ber_down',
  full_name='RAN_ber_down',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ue_info', full_name='RAN_ber_down.ue_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=522,
)


_RAN_MCS_UP = _descriptor.Descriptor(
  name='RAN_mcs_up',
  full_name='RAN_mcs_up',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ue_info', full_name='RAN_mcs_up.ue_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=565,
)


_RAN_MCS_DOWN = _descriptor.Descriptor(
  name='RAN_mcs_down',
  full_name='RAN_mcs_down',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ue_info', full_name='RAN_mcs_down.ue_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=567,
  serialized_end=610,
)


_RAN_MESSAGE = _descriptor.Descriptor(
  name='RAN_message',
  full_name='RAN_message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='RAN_message.msg_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_indication_request', full_name='RAN_message.ran_indication_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_indication_response', full_name='RAN_message.ran_indication_response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_control_request', full_name='RAN_message.ran_control_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_rsrp', full_name='RAN_message.ran_rsrp', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_ber_up', full_name='RAN_message.ran_ber_up', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_ber_down', full_name='RAN_message.ran_ber_down', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_mcs_up', full_name='RAN_message.ran_mcs_up', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ran_mcs_down', full_name='RAN_message.ran_mcs_down', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='RAN_message.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=613,
  serialized_end=1026,
)


_UE_INFO_M = _descriptor.Descriptor(
  name='ue_info_m',
  full_name='ue_info_m',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rnti', full_name='ue_info_m.rnti', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_rsrp', full_name='ue_info_m.ue_rsrp', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_ber_up', full_name='ue_info_m.ue_ber_up', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_ber_down', full_name='ue_info_m.ue_ber_down', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_mcs_up', full_name='ue_info_m.ue_mcs_up', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_mcs_down', full_name='ue_info_m.ue_mcs_down', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1028,
  serialized_end=1150,
)


_UE_LIST_M = _descriptor.Descriptor(
  name='ue_list_m',
  full_name='ue_list_m',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected_ues', full_name='ue_list_m.connected_ues', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocated_prbs', full_name='ue_list_m.allocated_prbs', index=1,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ue_info', full_name='ue_list_m.ue_info', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1152,
  serialized_end=1239,
)

_RAN_PARAM_MAP_ENTRY.fields_by_name['key'].enum_type = _RAN_PARAMETER
_RAN_PARAM_MAP_ENTRY.fields_by_name['ue_list'].message_type = _UE_LIST_M
_RAN_PARAM_MAP_ENTRY.oneofs_by_name['value'].fields.append(
  _RAN_PARAM_MAP_ENTRY.fields_by_name['int64_value'])
_RAN_PARAM_MAP_ENTRY.fields_by_name['int64_value'].containing_oneof = _RAN_PARAM_MAP_ENTRY.oneofs_by_name['value']
_RAN_PARAM_MAP_ENTRY.oneofs_by_name['value'].fields.append(
  _RAN_PARAM_MAP_ENTRY.fields_by_name['string_value'])
_RAN_PARAM_MAP_ENTRY.fields_by_name['string_value'].containing_oneof = _RAN_PARAM_MAP_ENTRY.oneofs_by_name['value']
_RAN_PARAM_MAP_ENTRY.oneofs_by_name['value'].fields.append(
  _RAN_PARAM_MAP_ENTRY.fields_by_name['ue_list'])
_RAN_PARAM_MAP_ENTRY.fields_by_name['ue_list'].containing_oneof = _RAN_PARAM_MAP_ENTRY.oneofs_by_name['value']
_RAN_INDICATION_REQUEST.fields_by_name['target_params'].enum_type = _RAN_PARAMETER
_RAN_INDICATION_RESPONSE.fields_by_name['param_map'].message_type = _RAN_PARAM_MAP_ENTRY
_RAN_INDICATION_RESPONSE.fields_by_name['ue_info'].message_type = _UE_INFO_M
_RAN_CONTROL_REQUEST.fields_by_name['target_param_map'].message_type = _RAN_PARAM_MAP_ENTRY
_RAN_RSRP.fields_by_name['ue_info'].message_type = _UE_INFO_M
_RAN_BER_UP.fields_by_name['ue_info'].message_type = _UE_INFO_M
_RAN_BER_DOWN.fields_by_name['ue_info'].message_type = _UE_INFO_M
_RAN_MCS_UP.fields_by_name['ue_info'].message_type = _UE_INFO_M
_RAN_MCS_DOWN.fields_by_name['ue_info'].message_type = _UE_INFO_M
_RAN_MESSAGE.fields_by_name['msg_type'].enum_type = _RAN_MESSAGE_TYPE
_RAN_MESSAGE.fields_by_name['ran_indication_request'].message_type = _RAN_INDICATION_REQUEST
_RAN_MESSAGE.fields_by_name['ran_indication_response'].message_type = _RAN_INDICATION_RESPONSE
_RAN_MESSAGE.fields_by_name['ran_control_request'].message_type = _RAN_CONTROL_REQUEST
_RAN_MESSAGE.fields_by_name['ran_rsrp'].message_type = _RAN_RSRP
_RAN_MESSAGE.fields_by_name['ran_ber_up'].message_type = _RAN_BER_UP
_RAN_MESSAGE.fields_by_name['ran_ber_down'].message_type = _RAN_BER_DOWN
_RAN_MESSAGE.fields_by_name['ran_mcs_up'].message_type = _RAN_MCS_UP
_RAN_MESSAGE.fields_by_name['ran_mcs_down'].message_type = _RAN_MCS_DOWN
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_indication_request'])
_RAN_MESSAGE.fields_by_name['ran_indication_request'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_indication_response'])
_RAN_MESSAGE.fields_by_name['ran_indication_response'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_control_request'])
_RAN_MESSAGE.fields_by_name['ran_control_request'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_rsrp'])
_RAN_MESSAGE.fields_by_name['ran_rsrp'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_ber_up'])
_RAN_MESSAGE.fields_by_name['ran_ber_up'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_ber_down'])
_RAN_MESSAGE.fields_by_name['ran_ber_down'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_mcs_up'])
_RAN_MESSAGE.fields_by_name['ran_mcs_up'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_RAN_MESSAGE.oneofs_by_name['payload'].fields.append(
  _RAN_MESSAGE.fields_by_name['ran_mcs_down'])
_RAN_MESSAGE.fields_by_name['ran_mcs_down'].containing_oneof = _RAN_MESSAGE.oneofs_by_name['payload']
_UE_LIST_M.fields_by_name['ue_info'].message_type = _UE_INFO_M
DESCRIPTOR.message_types_by_name['RAN_param_map_entry'] = _RAN_PARAM_MAP_ENTRY
DESCRIPTOR.message_types_by_name['RAN_indication_request'] = _RAN_INDICATION_REQUEST
DESCRIPTOR.message_types_by_name['RAN_indication_response'] = _RAN_INDICATION_RESPONSE
DESCRIPTOR.message_types_by_name['RAN_control_request'] = _RAN_CONTROL_REQUEST
DESCRIPTOR.message_types_by_name['RAN_rsrp'] = _RAN_RSRP
DESCRIPTOR.message_types_by_name['RAN_ber_up'] = _RAN_BER_UP
DESCRIPTOR.message_types_by_name['RAN_ber_down'] = _RAN_BER_DOWN
DESCRIPTOR.message_types_by_name['RAN_mcs_up'] = _RAN_MCS_UP
DESCRIPTOR.message_types_by_name['RAN_mcs_down'] = _RAN_MCS_DOWN
DESCRIPTOR.message_types_by_name['RAN_message'] = _RAN_MESSAGE
DESCRIPTOR.message_types_by_name['ue_info_m'] = _UE_INFO_M
DESCRIPTOR.message_types_by_name['ue_list_m'] = _UE_LIST_M
DESCRIPTOR.enum_types_by_name['RAN_message_type'] = _RAN_MESSAGE_TYPE
DESCRIPTOR.enum_types_by_name['RAN_parameter'] = _RAN_PARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RAN_param_map_entry = _reflection.GeneratedProtocolMessageType('RAN_param_map_entry', (_message.Message,), dict(
  DESCRIPTOR = _RAN_PARAM_MAP_ENTRY,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_param_map_entry)
  ))
_sym_db.RegisterMessage(RAN_param_map_entry)

RAN_indication_request = _reflection.GeneratedProtocolMessageType('RAN_indication_request', (_message.Message,), dict(
  DESCRIPTOR = _RAN_INDICATION_REQUEST,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_indication_request)
  ))
_sym_db.RegisterMessage(RAN_indication_request)

RAN_indication_response = _reflection.GeneratedProtocolMessageType('RAN_indication_response', (_message.Message,), dict(
  DESCRIPTOR = _RAN_INDICATION_RESPONSE,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_indication_response)
  ))
_sym_db.RegisterMessage(RAN_indication_response)

RAN_control_request = _reflection.GeneratedProtocolMessageType('RAN_control_request', (_message.Message,), dict(
  DESCRIPTOR = _RAN_CONTROL_REQUEST,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_control_request)
  ))
_sym_db.RegisterMessage(RAN_control_request)

RAN_rsrp = _reflection.GeneratedProtocolMessageType('RAN_rsrp', (_message.Message,), dict(
  DESCRIPTOR = _RAN_RSRP,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_rsrp)
  ))
_sym_db.RegisterMessage(RAN_rsrp)

RAN_ber_up = _reflection.GeneratedProtocolMessageType('RAN_ber_up', (_message.Message,), dict(
  DESCRIPTOR = _RAN_BER_UP,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_ber_up)
  ))
_sym_db.RegisterMessage(RAN_ber_up)

RAN_ber_down = _reflection.GeneratedProtocolMessageType('RAN_ber_down', (_message.Message,), dict(
  DESCRIPTOR = _RAN_BER_DOWN,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_ber_down)
  ))
_sym_db.RegisterMessage(RAN_ber_down)

RAN_mcs_up = _reflection.GeneratedProtocolMessageType('RAN_mcs_up', (_message.Message,), dict(
  DESCRIPTOR = _RAN_MCS_UP,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_mcs_up)
  ))
_sym_db.RegisterMessage(RAN_mcs_up)

RAN_mcs_down = _reflection.GeneratedProtocolMessageType('RAN_mcs_down', (_message.Message,), dict(
  DESCRIPTOR = _RAN_MCS_DOWN,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_mcs_down)
  ))
_sym_db.RegisterMessage(RAN_mcs_down)

RAN_message = _reflection.GeneratedProtocolMessageType('RAN_message', (_message.Message,), dict(
  DESCRIPTOR = _RAN_MESSAGE,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:RAN_message)
  ))
_sym_db.RegisterMessage(RAN_message)

ue_info_m = _reflection.GeneratedProtocolMessageType('ue_info_m', (_message.Message,), dict(
  DESCRIPTOR = _UE_INFO_M,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:ue_info_m)
  ))
_sym_db.RegisterMessage(ue_info_m)

ue_list_m = _reflection.GeneratedProtocolMessageType('ue_list_m', (_message.Message,), dict(
  DESCRIPTOR = _UE_LIST_M,
  __module__ = 'ran_messages_pb2'
  # @@protoc_insertion_point(class_scope:ue_list_m)
  ))
_sym_db.RegisterMessage(ue_list_m)


# @@protoc_insertion_point(module_scope)

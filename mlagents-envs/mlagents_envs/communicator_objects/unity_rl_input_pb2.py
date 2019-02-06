# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents/mlagents_envs/communicator_objects/unity_rl_input.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mlagents.envs.communicator_objects import agent_action_proto_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_agent__action__proto__pb2
from mlagents.envs.communicator_objects import environment_parameters_proto_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_environment__parameters__proto__pb2
from mlagents.envs.communicator_objects import command_proto_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_command__proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents/mlagents_envs/communicator_objects/unity_rl_input.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n7mlagents/mlagents_envs/communicator_objects/unity_rl_input.proto\x12\x14\x63ommunicator_objects\x1a;mlagents/mlagents_envs/communicator_objects/agent_action_proto.proto\x1a\x45mlagents/mlagents_envs/communicator_objects/environment_parameters_proto.proto\x1a\x36mlagents/mlagents_envs/communicator_objects/command_proto.proto\"\xb4\x03\n\x0cUnityRLInput\x12K\n\ragent_actions\x18\x01 \x03(\x0b\x32\x34.communicator_objects.UnityRLInput.AgentActionsEntry\x12P\n\x16\x65nvironment_parameters\x18\x02 \x01(\x0b\x32\x30.communicator_objects.EnvironmentParametersProto\x12\x13\n\x0bis_training\x18\x03 \x01(\x08\x12\x33\n\x07\x63ommand\x18\x04 \x01(\x0e\x32\".communicator_objects.CommandProto\x1aM\n\x14ListAgentActionProto\x12\x35\n\x05value\x18\x01 \x03(\x0b\x32&.communicator_objects.AgentActionProto\x1al\n\x11\x41gentActionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.communicator_objects.UnityRLInput.ListAgentActionProto:\x02\x38\x01\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[mlagents_dot_envs_dot_communicator__objects_dot_agent__action__proto__pb2.DESCRIPTOR,mlagents_dot_envs_dot_communicator__objects_dot_environment__parameters__proto__pb2.DESCRIPTOR,mlagents_dot_envs_dot_communicator__objects_dot_command__proto__pb2.DESCRIPTOR,])




_UNITYRLINPUT_LISTAGENTACTIONPROTO = _descriptor.Descriptor(
  name='ListAgentActionProto',
  full_name='communicator_objects.UnityRLInput.ListAgentActionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='communicator_objects.UnityRLInput.ListAgentActionProto.value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=596,
)

_UNITYRLINPUT_AGENTACTIONSENTRY = _descriptor.Descriptor(
  name='AgentActionsEntry',
  full_name='communicator_objects.UnityRLInput.AgentActionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='communicator_objects.UnityRLInput.AgentActionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='communicator_objects.UnityRLInput.AgentActionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=598,
  serialized_end=706,
)

_UNITYRLINPUT = _descriptor.Descriptor(
  name='UnityRLInput',
  full_name='communicator_objects.UnityRLInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_actions', full_name='communicator_objects.UnityRLInput.agent_actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment_parameters', full_name='communicator_objects.UnityRLInput.environment_parameters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_training', full_name='communicator_objects.UnityRLInput.is_training', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='communicator_objects.UnityRLInput.command', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UNITYRLINPUT_LISTAGENTACTIONPROTO, _UNITYRLINPUT_AGENTACTIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=706,
)

_UNITYRLINPUT_LISTAGENTACTIONPROTO.fields_by_name['value'].message_type = mlagents_dot_envs_dot_communicator__objects_dot_agent__action__proto__pb2._AGENTACTIONPROTO
_UNITYRLINPUT_LISTAGENTACTIONPROTO.containing_type = _UNITYRLINPUT
_UNITYRLINPUT_AGENTACTIONSENTRY.fields_by_name['value'].message_type = _UNITYRLINPUT_LISTAGENTACTIONPROTO
_UNITYRLINPUT_AGENTACTIONSENTRY.containing_type = _UNITYRLINPUT
_UNITYRLINPUT.fields_by_name['agent_actions'].message_type = _UNITYRLINPUT_AGENTACTIONSENTRY
_UNITYRLINPUT.fields_by_name['environment_parameters'].message_type = mlagents_dot_envs_dot_communicator__objects_dot_environment__parameters__proto__pb2._ENVIRONMENTPARAMETERSPROTO
_UNITYRLINPUT.fields_by_name['command'].enum_type = mlagents_dot_envs_dot_communicator__objects_dot_command__proto__pb2._COMMANDPROTO
DESCRIPTOR.message_types_by_name['UnityRLInput'] = _UNITYRLINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityRLInput = _reflection.GeneratedProtocolMessageType('UnityRLInput', (_message.Message,), dict(

  ListAgentActionProto = _reflection.GeneratedProtocolMessageType('ListAgentActionProto', (_message.Message,), dict(
    DESCRIPTOR = _UNITYRLINPUT_LISTAGENTACTIONPROTO,
    __module__ = 'mlagents.mlagents_envs.communicator_objects.unity_rl_input_pb2'
    # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLInput.ListAgentActionProto)
    ))
  ,

  AgentActionsEntry = _reflection.GeneratedProtocolMessageType('AgentActionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _UNITYRLINPUT_AGENTACTIONSENTRY,
    __module__ = 'mlagents.mlagents_envs.communicator_objects.unity_rl_input_pb2'
    # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLInput.AgentActionsEntry)
    ))
  ,
  DESCRIPTOR = _UNITYRLINPUT,
  __module__ = 'mlagents.mlagents_envs.communicator_objects.unity_rl_input_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLInput)
  ))
_sym_db.RegisterMessage(UnityRLInput)
_sym_db.RegisterMessage(UnityRLInput.ListAgentActionProto)
_sym_db.RegisterMessage(UnityRLInput.AgentActionsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\034MLAgents.CommunicatorObjects'))
_UNITYRLINPUT_AGENTACTIONSENTRY.has_options = True
_UNITYRLINPUT_AGENTACTIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
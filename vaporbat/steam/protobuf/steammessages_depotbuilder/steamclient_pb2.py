# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_depotbuilder.steamclient.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steammessages_unified_base import steamclient_pb2 as steammessages__unified__base_dot_steamclient__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_depotbuilder.steamclient.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n,steammessages_depotbuilder.steamclient.proto\x1a,steammessages_unified_base.steamclient.proto\"w\n&CContentBuilder_InitDepotBuild_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x17\n\x0fworkshop_itemid\x18\x03 \x01(\x04\x12\x14\n\x0c\x66or_local_cs\x18\x04 \x01(\x08\"\x8e\x01\n\'CContentBuilder_InitDepotBuild_Response\x12\x1b\n\x13\x62\x61seline_manifestid\x18\x01 \x01(\x04\x12\x12\n\nchunk_size\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x65s_key\x18\x03 \x01(\x0c\x12\x0f\n\x07rsa_key\x18\x04 \x01(\x0c\x12\x10\n\x08url_host\x18\x05 \x01(\t\"\xad\x01\n(CContentBuilder_StartDepotUpload_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x17\n\x0fworkshop_itemid\x18\x03 \x01(\x04\x12\x14\n\x0c\x66or_local_cs\x18\x04 \x01(\x08\x12\x1b\n\x13\x62\x61seline_manifestid\x18\x05 \x01(\x04\x12\x15\n\rmanifest_size\x18\x06 \x01(\r\"G\n)CContentBuilder_StartDepotUpload_Response\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x01 \x01(\x04\"Z\n-CContentBuilder_GetMissingDepotChunks_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x02 \x01(\x04\"\xd2\x01\n.CContentBuilder_GetMissingDepotChunks_Response\x12N\n\x0emissing_chunks\x18\x01 \x03(\x0b\x32\x36.CContentBuilder_GetMissingDepotChunks_Response.Chunks\x12\x1c\n\x14total_missing_chunks\x18\x02 \x01(\r\x12\x1b\n\x13total_missing_bytes\x18\x03 \x01(\x04\x1a\x15\n\x06\x43hunks\x12\x0b\n\x03sha\x18\x01 \x01(\x0c\"V\n)CContentBuilder_FinishDepotUpload_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x1a\n\x12\x64\x65pot_build_handle\x18\x02 \x01(\x04\"U\n*CContentBuilder_FinishDepotUpload_Response\x12\x12\n\nmanifestid\x18\x01 \x01(\x04\x12\x13\n\x0bprev_reused\x18\x02 \x01(\x08\"\xd9\x01\n&CContentBuilder_CommitAppBuild_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12G\n\x0f\x64\x65pot_manifests\x18\x02 \x03(\x0b\x32..CContentBuilder_CommitAppBuild_Request.Depots\x12\x13\n\x0b\x62uild_notes\x18\x04 \x01(\t\x12\x13\n\x0blive_branch\x18\x05 \x01(\t\x1a-\n\x06\x44\x65pots\x12\x0f\n\x07\x64\x65potid\x18\x01 \x01(\r\x12\x12\n\nmanifestid\x18\x02 \x01(\x04\":\n\'CContentBuilder_CommitAppBuild_Response\x12\x0f\n\x07\x62uildid\x18\x01 \x01(\r\"c\n)CContentBuilder_SignInstallScript_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x16\n\x0einstall_script\x18\x03 \x01(\t\"K\n*CContentBuilder_SignInstallScript_Response\x12\x1d\n\x15signed_install_script\x18\x01 \x01(\t2\x92\x08\n\x0e\x43ontentBuilder\x12\x98\x01\n\x0eInitDepotBuild\x12\'.CContentBuilder_InitDepotBuild_Request\x1a(.CContentBuilder_InitDepotBuild_Response\"3\x82\xb5\x18/Get inital parameters to start building a depot\x12\x9e\x01\n\x10StartDepotUpload\x12).CContentBuilder_StartDepotUpload_Request\x1a*.CContentBuilder_StartDepotUpload_Response\"3\x82\xb5\x18/Start uploading manifest and chunks for a depot\x12\xa9\x01\n\x15GetMissingDepotChunks\x12..CContentBuilder_GetMissingDepotChunks_Request\x1a/.CContentBuilder_GetMissingDepotChunks_Response\"/\x82\xb5\x18+Get list of missing chunks for depot upload\x12\xb1\x01\n\x11\x46inishDepotUpload\x12*.CContentBuilder_FinishDepotUpload_Request\x1a+.CContentBuilder_FinishDepotUpload_Response\"C\x82\xb5\x18?Commit a depot build after manifest and all chunks are uploaded\x12\xa7\x01\n\x0e\x43ommitAppBuild\x12\'.CContentBuilder_CommitAppBuild_Request\x1a(.CContentBuilder_CommitAppBuild_Response\"B\x82\xb5\x18>Combine previous depot uploads into an app build and commit it\x12\x88\x01\n\x11SignInstallScript\x12*.CContentBuilder_SignInstallScript_Request\x1a+.CContentBuilder_SignInstallScript_Response\"\x1a\x82\xb5\x18\x16Sign an install script\x1a/\x82\xb5\x18+Interface to build and upload depot contentB\x03\x80\x01\x01')
  ,
  dependencies=[steammessages__unified__base_dot_steamclient__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CCONTENTBUILDER_INITDEPOTBUILD_REQUEST = _descriptor.Descriptor(
  name='CContentBuilder_InitDepotBuild_Request',
  full_name='CContentBuilder_InitDepotBuild_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CContentBuilder_InitDepotBuild_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depotid', full_name='CContentBuilder_InitDepotBuild_Request.depotid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workshop_itemid', full_name='CContentBuilder_InitDepotBuild_Request.workshop_itemid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='for_local_cs', full_name='CContentBuilder_InitDepotBuild_Request.for_local_cs', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=213,
)


_CCONTENTBUILDER_INITDEPOTBUILD_RESPONSE = _descriptor.Descriptor(
  name='CContentBuilder_InitDepotBuild_Response',
  full_name='CContentBuilder_InitDepotBuild_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='baseline_manifestid', full_name='CContentBuilder_InitDepotBuild_Response.baseline_manifestid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunk_size', full_name='CContentBuilder_InitDepotBuild_Response.chunk_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aes_key', full_name='CContentBuilder_InitDepotBuild_Response.aes_key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rsa_key', full_name='CContentBuilder_InitDepotBuild_Response.rsa_key', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url_host', full_name='CContentBuilder_InitDepotBuild_Response.url_host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=358,
)


_CCONTENTBUILDER_STARTDEPOTUPLOAD_REQUEST = _descriptor.Descriptor(
  name='CContentBuilder_StartDepotUpload_Request',
  full_name='CContentBuilder_StartDepotUpload_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CContentBuilder_StartDepotUpload_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depotid', full_name='CContentBuilder_StartDepotUpload_Request.depotid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workshop_itemid', full_name='CContentBuilder_StartDepotUpload_Request.workshop_itemid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='for_local_cs', full_name='CContentBuilder_StartDepotUpload_Request.for_local_cs', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baseline_manifestid', full_name='CContentBuilder_StartDepotUpload_Request.baseline_manifestid', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manifest_size', full_name='CContentBuilder_StartDepotUpload_Request.manifest_size', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=534,
)


_CCONTENTBUILDER_STARTDEPOTUPLOAD_RESPONSE = _descriptor.Descriptor(
  name='CContentBuilder_StartDepotUpload_Response',
  full_name='CContentBuilder_StartDepotUpload_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='depot_build_handle', full_name='CContentBuilder_StartDepotUpload_Response.depot_build_handle', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=607,
)


_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_REQUEST = _descriptor.Descriptor(
  name='CContentBuilder_GetMissingDepotChunks_Request',
  full_name='CContentBuilder_GetMissingDepotChunks_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CContentBuilder_GetMissingDepotChunks_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depot_build_handle', full_name='CContentBuilder_GetMissingDepotChunks_Request.depot_build_handle', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=699,
)


_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS = _descriptor.Descriptor(
  name='Chunks',
  full_name='CContentBuilder_GetMissingDepotChunks_Response.Chunks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sha', full_name='CContentBuilder_GetMissingDepotChunks_Response.Chunks.sha', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=891,
  serialized_end=912,
)

_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE = _descriptor.Descriptor(
  name='CContentBuilder_GetMissingDepotChunks_Response',
  full_name='CContentBuilder_GetMissingDepotChunks_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='missing_chunks', full_name='CContentBuilder_GetMissingDepotChunks_Response.missing_chunks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_missing_chunks', full_name='CContentBuilder_GetMissingDepotChunks_Response.total_missing_chunks', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_missing_bytes', full_name='CContentBuilder_GetMissingDepotChunks_Response.total_missing_bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=912,
)


_CCONTENTBUILDER_FINISHDEPOTUPLOAD_REQUEST = _descriptor.Descriptor(
  name='CContentBuilder_FinishDepotUpload_Request',
  full_name='CContentBuilder_FinishDepotUpload_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CContentBuilder_FinishDepotUpload_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depot_build_handle', full_name='CContentBuilder_FinishDepotUpload_Request.depot_build_handle', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=914,
  serialized_end=1000,
)


_CCONTENTBUILDER_FINISHDEPOTUPLOAD_RESPONSE = _descriptor.Descriptor(
  name='CContentBuilder_FinishDepotUpload_Response',
  full_name='CContentBuilder_FinishDepotUpload_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manifestid', full_name='CContentBuilder_FinishDepotUpload_Response.manifestid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_reused', full_name='CContentBuilder_FinishDepotUpload_Response.prev_reused', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1002,
  serialized_end=1087,
)


_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS = _descriptor.Descriptor(
  name='Depots',
  full_name='CContentBuilder_CommitAppBuild_Request.Depots',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='depotid', full_name='CContentBuilder_CommitAppBuild_Request.Depots.depotid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manifestid', full_name='CContentBuilder_CommitAppBuild_Request.Depots.manifestid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1262,
  serialized_end=1307,
)

_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST = _descriptor.Descriptor(
  name='CContentBuilder_CommitAppBuild_Request',
  full_name='CContentBuilder_CommitAppBuild_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CContentBuilder_CommitAppBuild_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depot_manifests', full_name='CContentBuilder_CommitAppBuild_Request.depot_manifests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_notes', full_name='CContentBuilder_CommitAppBuild_Request.build_notes', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='live_branch', full_name='CContentBuilder_CommitAppBuild_Request.live_branch', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1090,
  serialized_end=1307,
)


_CCONTENTBUILDER_COMMITAPPBUILD_RESPONSE = _descriptor.Descriptor(
  name='CContentBuilder_CommitAppBuild_Response',
  full_name='CContentBuilder_CommitAppBuild_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buildid', full_name='CContentBuilder_CommitAppBuild_Response.buildid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1309,
  serialized_end=1367,
)


_CCONTENTBUILDER_SIGNINSTALLSCRIPT_REQUEST = _descriptor.Descriptor(
  name='CContentBuilder_SignInstallScript_Request',
  full_name='CContentBuilder_SignInstallScript_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CContentBuilder_SignInstallScript_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depotid', full_name='CContentBuilder_SignInstallScript_Request.depotid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='install_script', full_name='CContentBuilder_SignInstallScript_Request.install_script', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1369,
  serialized_end=1468,
)


_CCONTENTBUILDER_SIGNINSTALLSCRIPT_RESPONSE = _descriptor.Descriptor(
  name='CContentBuilder_SignInstallScript_Response',
  full_name='CContentBuilder_SignInstallScript_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_install_script', full_name='CContentBuilder_SignInstallScript_Response.signed_install_script', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1470,
  serialized_end=1545,
)

_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS.containing_type = _CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE
_CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE.fields_by_name['missing_chunks'].message_type = _CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS
_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS.containing_type = _CCONTENTBUILDER_COMMITAPPBUILD_REQUEST
_CCONTENTBUILDER_COMMITAPPBUILD_REQUEST.fields_by_name['depot_manifests'].message_type = _CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS
DESCRIPTOR.message_types_by_name['CContentBuilder_InitDepotBuild_Request'] = _CCONTENTBUILDER_INITDEPOTBUILD_REQUEST
DESCRIPTOR.message_types_by_name['CContentBuilder_InitDepotBuild_Response'] = _CCONTENTBUILDER_INITDEPOTBUILD_RESPONSE
DESCRIPTOR.message_types_by_name['CContentBuilder_StartDepotUpload_Request'] = _CCONTENTBUILDER_STARTDEPOTUPLOAD_REQUEST
DESCRIPTOR.message_types_by_name['CContentBuilder_StartDepotUpload_Response'] = _CCONTENTBUILDER_STARTDEPOTUPLOAD_RESPONSE
DESCRIPTOR.message_types_by_name['CContentBuilder_GetMissingDepotChunks_Request'] = _CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_REQUEST
DESCRIPTOR.message_types_by_name['CContentBuilder_GetMissingDepotChunks_Response'] = _CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE
DESCRIPTOR.message_types_by_name['CContentBuilder_FinishDepotUpload_Request'] = _CCONTENTBUILDER_FINISHDEPOTUPLOAD_REQUEST
DESCRIPTOR.message_types_by_name['CContentBuilder_FinishDepotUpload_Response'] = _CCONTENTBUILDER_FINISHDEPOTUPLOAD_RESPONSE
DESCRIPTOR.message_types_by_name['CContentBuilder_CommitAppBuild_Request'] = _CCONTENTBUILDER_COMMITAPPBUILD_REQUEST
DESCRIPTOR.message_types_by_name['CContentBuilder_CommitAppBuild_Response'] = _CCONTENTBUILDER_COMMITAPPBUILD_RESPONSE
DESCRIPTOR.message_types_by_name['CContentBuilder_SignInstallScript_Request'] = _CCONTENTBUILDER_SIGNINSTALLSCRIPT_REQUEST
DESCRIPTOR.message_types_by_name['CContentBuilder_SignInstallScript_Response'] = _CCONTENTBUILDER_SIGNINSTALLSCRIPT_RESPONSE

CContentBuilder_InitDepotBuild_Request = _reflection.GeneratedProtocolMessageType('CContentBuilder_InitDepotBuild_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_INITDEPOTBUILD_REQUEST,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_InitDepotBuild_Request)
  ))
_sym_db.RegisterMessage(CContentBuilder_InitDepotBuild_Request)

CContentBuilder_InitDepotBuild_Response = _reflection.GeneratedProtocolMessageType('CContentBuilder_InitDepotBuild_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_INITDEPOTBUILD_RESPONSE,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_InitDepotBuild_Response)
  ))
_sym_db.RegisterMessage(CContentBuilder_InitDepotBuild_Response)

CContentBuilder_StartDepotUpload_Request = _reflection.GeneratedProtocolMessageType('CContentBuilder_StartDepotUpload_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_STARTDEPOTUPLOAD_REQUEST,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_StartDepotUpload_Request)
  ))
_sym_db.RegisterMessage(CContentBuilder_StartDepotUpload_Request)

CContentBuilder_StartDepotUpload_Response = _reflection.GeneratedProtocolMessageType('CContentBuilder_StartDepotUpload_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_STARTDEPOTUPLOAD_RESPONSE,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_StartDepotUpload_Response)
  ))
_sym_db.RegisterMessage(CContentBuilder_StartDepotUpload_Response)

CContentBuilder_GetMissingDepotChunks_Request = _reflection.GeneratedProtocolMessageType('CContentBuilder_GetMissingDepotChunks_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_REQUEST,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_GetMissingDepotChunks_Request)
  ))
_sym_db.RegisterMessage(CContentBuilder_GetMissingDepotChunks_Request)

CContentBuilder_GetMissingDepotChunks_Response = _reflection.GeneratedProtocolMessageType('CContentBuilder_GetMissingDepotChunks_Response', (_message.Message,), dict(

  Chunks = _reflection.GeneratedProtocolMessageType('Chunks', (_message.Message,), dict(
    DESCRIPTOR = _CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE_CHUNKS,
    __module__ = 'steammessages_depotbuilder.steamclient_pb2'
    # @@protoc_insertion_point(class_scope:CContentBuilder_GetMissingDepotChunks_Response.Chunks)
    ))
  ,
  DESCRIPTOR = _CCONTENTBUILDER_GETMISSINGDEPOTCHUNKS_RESPONSE,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_GetMissingDepotChunks_Response)
  ))
_sym_db.RegisterMessage(CContentBuilder_GetMissingDepotChunks_Response)
_sym_db.RegisterMessage(CContentBuilder_GetMissingDepotChunks_Response.Chunks)

CContentBuilder_FinishDepotUpload_Request = _reflection.GeneratedProtocolMessageType('CContentBuilder_FinishDepotUpload_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_FINISHDEPOTUPLOAD_REQUEST,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_FinishDepotUpload_Request)
  ))
_sym_db.RegisterMessage(CContentBuilder_FinishDepotUpload_Request)

CContentBuilder_FinishDepotUpload_Response = _reflection.GeneratedProtocolMessageType('CContentBuilder_FinishDepotUpload_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_FINISHDEPOTUPLOAD_RESPONSE,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_FinishDepotUpload_Response)
  ))
_sym_db.RegisterMessage(CContentBuilder_FinishDepotUpload_Response)

CContentBuilder_CommitAppBuild_Request = _reflection.GeneratedProtocolMessageType('CContentBuilder_CommitAppBuild_Request', (_message.Message,), dict(

  Depots = _reflection.GeneratedProtocolMessageType('Depots', (_message.Message,), dict(
    DESCRIPTOR = _CCONTENTBUILDER_COMMITAPPBUILD_REQUEST_DEPOTS,
    __module__ = 'steammessages_depotbuilder.steamclient_pb2'
    # @@protoc_insertion_point(class_scope:CContentBuilder_CommitAppBuild_Request.Depots)
    ))
  ,
  DESCRIPTOR = _CCONTENTBUILDER_COMMITAPPBUILD_REQUEST,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_CommitAppBuild_Request)
  ))
_sym_db.RegisterMessage(CContentBuilder_CommitAppBuild_Request)
_sym_db.RegisterMessage(CContentBuilder_CommitAppBuild_Request.Depots)

CContentBuilder_CommitAppBuild_Response = _reflection.GeneratedProtocolMessageType('CContentBuilder_CommitAppBuild_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_COMMITAPPBUILD_RESPONSE,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_CommitAppBuild_Response)
  ))
_sym_db.RegisterMessage(CContentBuilder_CommitAppBuild_Response)

CContentBuilder_SignInstallScript_Request = _reflection.GeneratedProtocolMessageType('CContentBuilder_SignInstallScript_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_SIGNINSTALLSCRIPT_REQUEST,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_SignInstallScript_Request)
  ))
_sym_db.RegisterMessage(CContentBuilder_SignInstallScript_Request)

CContentBuilder_SignInstallScript_Response = _reflection.GeneratedProtocolMessageType('CContentBuilder_SignInstallScript_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCONTENTBUILDER_SIGNINSTALLSCRIPT_RESPONSE,
  __module__ = 'steammessages_depotbuilder.steamclient_pb2'
  # @@protoc_insertion_point(class_scope:CContentBuilder_SignInstallScript_Response)
  ))
_sym_db.RegisterMessage(CContentBuilder_SignInstallScript_Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\200\001\001'))
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/resources/user_interest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.common import criterion_category_availability_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_criterion__category__availability__pb2
from google.ads.google_ads.v5.proto.enums import user_interest_taxonomy_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_user__interest__taxonomy__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/resources/user_interest.proto',
  package='google.ads.googleads.v5.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v5.resourcesB\021UserInterestProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V5.Resources\312\002!Google\\Ads\\GoogleAds\\V5\\Resources\352\002%Google::Ads::GoogleAds::V5::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads_v5/proto/resources/user_interest.proto\x12!google.ads.googleads.v5.resources\x1aJgoogle/ads/googleads_v5/proto/common/criterion_category_availability.proto\x1a\x45google/ads/googleads_v5/proto/enums/user_interest_taxonomy_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\x94\x05\n\x0cUserInterest\x12\x44\n\rresource_name\x18\x01 \x01(\tB-\xe0\x41\x03\xfa\x41\'\n%googleads.googleapis.com/UserInterest\x12p\n\rtaxonomy_type\x18\x02 \x01(\x0e\x32T.google.ads.googleads.v5.enums.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeB\x03\xe0\x41\x03\x12:\n\x10user_interest_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12/\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12i\n\x14user_interest_parent\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueB-\xe0\x41\x03\xfa\x41\'\n%googleads.googleapis.com/UserInterest\x12\x38\n\x0flaunched_to_all\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x03\xe0\x41\x03\x12Z\n\x0e\x61vailabilities\x18\x07 \x03(\x0b\x32=.google.ads.googleads.v5.common.CriterionCategoryAvailabilityB\x03\xe0\x41\x03:^\xea\x41[\n%googleads.googleapis.com/UserInterest\x12\x32\x63ustomers/{customer}/userInterests/{user_interest}B\xfe\x01\n%com.google.ads.googleads.v5.resourcesB\x11UserInterestProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V5.Resources\xca\x02!Google\\Ads\\GoogleAds\\V5\\Resources\xea\x02%Google::Ads::GoogleAds::V5::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_criterion__category__availability__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_user__interest__taxonomy__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_USERINTEREST = _descriptor.Descriptor(
  name='UserInterest',
  full_name='google.ads.googleads.v5.resources.UserInterest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.resources.UserInterest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A\'\n%googleads.googleapis.com/UserInterest', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='taxonomy_type', full_name='google.ads.googleads.v5.resources.UserInterest.taxonomy_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_interest_id', full_name='google.ads.googleads.v5.resources.UserInterest.user_interest_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v5.resources.UserInterest.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_interest_parent', full_name='google.ads.googleads.v5.resources.UserInterest.user_interest_parent', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A\'\n%googleads.googleapis.com/UserInterest', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='launched_to_all', full_name='google.ads.googleads.v5.resources.UserInterest.launched_to_all', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='availabilities', full_name='google.ads.googleads.v5.resources.UserInterest.availabilities', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A[\n%googleads.googleapis.com/UserInterest\0222customers/{customer}/userInterests/{user_interest}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=1028,
)

_USERINTEREST.fields_by_name['taxonomy_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_user__interest__taxonomy__type__pb2._USERINTERESTTAXONOMYTYPEENUM_USERINTERESTTAXONOMYTYPE
_USERINTEREST.fields_by_name['user_interest_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_USERINTEREST.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_USERINTEREST.fields_by_name['user_interest_parent'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_USERINTEREST.fields_by_name['launched_to_all'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_USERINTEREST.fields_by_name['availabilities'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_criterion__category__availability__pb2._CRITERIONCATEGORYAVAILABILITY
DESCRIPTOR.message_types_by_name['UserInterest'] = _USERINTEREST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserInterest = _reflection.GeneratedProtocolMessageType('UserInterest', (_message.Message,), {
  'DESCRIPTOR' : _USERINTEREST,
  '__module__' : 'google.ads.googleads_v5.proto.resources.user_interest_pb2'
  ,
  '__doc__': """A user interest: a particular interest-based vertical to be targeted.
  
  Attributes:
      resource_name:
          Output only. The resource name of the user interest. User
          interest resource names have the form:
          ``customers/{customer_id}/userInterests/{user_interest_id}``
      taxonomy_type:
          Output only. Taxonomy type of the user interest.
      user_interest_id:
          Output only. The ID of the user interest.
      name:
          Output only. The name of the user interest.
      user_interest_parent:
          Output only. The parent of the user interest.
      launched_to_all:
          Output only. True if the user interest is launched to all
          channels and locales.
      availabilities:
          Output only. Availability information of the user interest.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.resources.UserInterest)
  })
_sym_db.RegisterMessage(UserInterest)


DESCRIPTOR._options = None
_USERINTEREST.fields_by_name['resource_name']._options = None
_USERINTEREST.fields_by_name['taxonomy_type']._options = None
_USERINTEREST.fields_by_name['user_interest_id']._options = None
_USERINTEREST.fields_by_name['name']._options = None
_USERINTEREST.fields_by_name['user_interest_parent']._options = None
_USERINTEREST.fields_by_name['launched_to_all']._options = None
_USERINTEREST.fields_by_name['availabilities']._options = None
_USERINTEREST._options = None
# @@protoc_insertion_point(module_scope)
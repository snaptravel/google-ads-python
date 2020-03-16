# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/errors/feed_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/errors/feed_error.proto',
  package='google.ads.googleads.v3.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v3.errorsB\016FeedErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V3.Errors\312\002\036Google\\Ads\\GoogleAds\\V3\\Errors\352\002\"Google::Ads::GoogleAds::V3::Errors'),
  serialized_pb=_b('\n5google/ads/googleads_v3/proto/errors/feed_error.proto\x12\x1egoogle.ads.googleads.v3.errors\x1a\x1cgoogle/api/annotations.proto\"\xc6\x06\n\rFeedErrorEnum\"\xb4\x06\n\tFeedError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1e\n\x1a\x41TTRIBUTE_NAMES_NOT_UNIQUE\x10\x02\x12/\n+ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES\x10\x03\x12.\n*CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED\x10\x04\x12\x34\n0CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED\x10\x05\x12\x32\n.CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED\x10\x06\x12\x34\n0CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE\x10\x07\x12\x10\n\x0c\x46\x45\x45\x44_REMOVED\x10\x08\x12\x18\n\x14INVALID_ORIGIN_VALUE\x10\t\x12\x1b\n\x17\x46\x45\x45\x44_ORIGIN_IS_NOT_USER\x10\n\x12 \n\x1cINVALID_AUTH_TOKEN_FOR_EMAIL\x10\x0b\x12\x11\n\rINVALID_EMAIL\x10\x0c\x12\x17\n\x13\x44UPLICATE_FEED_NAME\x10\r\x12\x15\n\x11INVALID_FEED_NAME\x10\x0e\x12\x16\n\x12MISSING_OAUTH_INFO\x10\x0f\x12.\n*NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY\x10\x10\x12\x17\n\x13TOO_MANY_ATTRIBUTES\x10\x11\x12\x1c\n\x18INVALID_BUSINESS_ACCOUNT\x10\x12\x12\x33\n/BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT\x10\x13\x12\x1e\n\x1aINVALID_AFFILIATE_CHAIN_ID\x10\x14\x12\x19\n\x15\x44UPLICATE_SYSTEM_FEED\x10\x15\x12\x14\n\x10GMB_ACCESS_ERROR\x10\x16\x12\x35\n1CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS\x10\x17\x42\xe9\x01\n\"com.google.ads.googleads.v3.errorsB\x0e\x46\x65\x65\x64\x45rrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V3.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V3\\Errors\xea\x02\"Google::Ads::GoogleAds::V3::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDERRORENUM_FEEDERROR = _descriptor.EnumDescriptor(
  name='FeedError',
  full_name='google.ads.googleads.v3.errors.FeedErrorEnum.FeedError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTRIBUTE_NAMES_NOT_UNIQUE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_REMOVED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ORIGIN_VALUE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_ORIGIN_IS_NOT_USER', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AUTH_TOKEN_FOR_EMAIL', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_EMAIL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_FEED_NAME', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FEED_NAME', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_OAUTH_INFO', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_ATTRIBUTES', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_BUSINESS_ACCOUNT', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AFFILIATE_CHAIN_ID', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_SYSTEM_FEED', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GMB_ACCESS_ERROR', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS', index=23, number=23,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=138,
  serialized_end=958,
)
_sym_db.RegisterEnumDescriptor(_FEEDERRORENUM_FEEDERROR)


_FEEDERRORENUM = _descriptor.Descriptor(
  name='FeedErrorEnum',
  full_name='google.ads.googleads.v3.errors.FeedErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDERRORENUM_FEEDERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=958,
)

_FEEDERRORENUM_FEEDERROR.containing_type = _FEEDERRORENUM
DESCRIPTOR.message_types_by_name['FeedErrorEnum'] = _FEEDERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedErrorEnum = _reflection.GeneratedProtocolMessageType('FeedErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDERRORENUM,
  __module__ = 'google.ads.googleads_v3.proto.errors.feed_error_pb2'
  ,
  __doc__ = """Container for enum describing possible feed errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.errors.FeedErrorEnum)
  ))
_sym_db.RegisterMessage(FeedErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
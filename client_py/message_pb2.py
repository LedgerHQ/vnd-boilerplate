# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"\x13\n\x11RequestGetVersion\"%\n\x12ResponseGetVersion\x12\x0f\n\x07version\x18\x01 \x01(\t\"\x11\n\x0fRequestInitSwap\"%\n\x10ResponseInitSwap\x12\x11\n\tdevice_id\x18\x01 \x01(\x0c\"\x11\n\x0fRequestInitSell\"%\n\x10ResponseInitSell\x12\x11\n\tdevice_id\x18\x01 \x01(\x0c\":\n\x07Partner\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06pubkey\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"\xb9\x01\n\x0bRequestSwap\x12\x19\n\x07partner\x18\x01 \x01(\x0b\x32\x08.Partner\x12\r\n\x05pb_tx\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x12\x0b\n\x03\x66\x65\x65\x18\x04 \x01(\x0c\x12\x13\n\x0bpayout_path\x18\x05 \x03(\r\x12\x13\n\x0brefund_path\x18\x06 \x03(\r\x12\x1a\n\x12payout_addr_params\x18\x07 \x01(\x0c\x12\x1a\n\x12refund_addr_params\x18\x08 \x01(\x0c\",\n\x0cResponseSwap\x12\x10\n\x08\x61pproved\x18\x01 \x01(\x08\x12\n\n\x02tx\x18\x02 \x01(\x0c\"X\n\x0bRequestSell\x12\x19\n\x07partner\x18\x01 \x01(\x0b\x32\x08.Partner\x12\x0e\n\x06\x62\x36\x34_tx\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x12\x0b\n\x03\x66\x65\x65\x18\x04 \x01(\x0c\"3\n\x0cResponseSell\x12\x10\n\x08\x61pproved\x18\x01 \x01(\x08\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\"\n\rResponseError\x12\x11\n\terror_msg\x18\x01 \x01(\t\"\xc9\x01\n\x07Request\x12)\n\x0bget_version\x18\x01 \x01(\x0b\x32\x12.RequestGetVersionH\x00\x12%\n\tinit_swap\x18\x02 \x01(\x0b\x32\x10.RequestInitSwapH\x00\x12%\n\tinit_sell\x18\x03 \x01(\x0b\x32\x10.RequestInitSellH\x00\x12\x1c\n\x04swap\x18\x04 \x01(\x0b\x32\x0c.RequestSwapH\x00\x12\x1c\n\x04sell\x18\x05 \x01(\x0b\x32\x0c.RequestSellH\x00\x42\t\n\x07request\"\xf1\x01\n\x08Response\x12*\n\x0bget_version\x18\x01 \x01(\x0b\x32\x13.ResponseGetVersionH\x00\x12&\n\tinit_swap\x18\x02 \x01(\x0b\x32\x11.ResponseInitSwapH\x00\x12&\n\tinit_sell\x18\x03 \x01(\x0b\x32\x11.ResponseInitSellH\x00\x12\x1d\n\x04swap\x18\x04 \x01(\x0b\x32\r.ResponseSwapH\x00\x12\x1d\n\x04sell\x18\x05 \x01(\x0b\x32\r.ResponseSellH\x00\x12\x1f\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x0e.ResponseErrorH\x00\x42\n\n\x08responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUESTGETVERSION']._serialized_start=17
  _globals['_REQUESTGETVERSION']._serialized_end=36
  _globals['_RESPONSEGETVERSION']._serialized_start=38
  _globals['_RESPONSEGETVERSION']._serialized_end=75
  _globals['_REQUESTINITSWAP']._serialized_start=77
  _globals['_REQUESTINITSWAP']._serialized_end=94
  _globals['_RESPONSEINITSWAP']._serialized_start=96
  _globals['_RESPONSEINITSWAP']._serialized_end=133
  _globals['_REQUESTINITSELL']._serialized_start=135
  _globals['_REQUESTINITSELL']._serialized_end=152
  _globals['_RESPONSEINITSELL']._serialized_start=154
  _globals['_RESPONSEINITSELL']._serialized_end=191
  _globals['_PARTNER']._serialized_start=193
  _globals['_PARTNER']._serialized_end=251
  _globals['_REQUESTSWAP']._serialized_start=254
  _globals['_REQUESTSWAP']._serialized_end=439
  _globals['_RESPONSESWAP']._serialized_start=441
  _globals['_RESPONSESWAP']._serialized_end=485
  _globals['_REQUESTSELL']._serialized_start=487
  _globals['_REQUESTSELL']._serialized_end=575
  _globals['_RESPONSESELL']._serialized_start=577
  _globals['_RESPONSESELL']._serialized_end=628
  _globals['_RESPONSEERROR']._serialized_start=630
  _globals['_RESPONSEERROR']._serialized_end=664
  _globals['_REQUEST']._serialized_start=667
  _globals['_REQUEST']._serialized_end=868
  _globals['_RESPONSE']._serialized_start=871
  _globals['_RESPONSE']._serialized_end=1112
# @@protoc_insertion_point(module_scope)

/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: ran_messages.proto */

#ifndef PROTOBUF_C_ran_5fmessages_2eproto__INCLUDED
#define PROTOBUF_C_ran_5fmessages_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1000000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif


typedef struct _RANParamMapEntry RANParamMapEntry;
typedef struct _RANIndicationRequest RANIndicationRequest;
typedef struct _RANIndicationResponse RANIndicationResponse;
typedef struct _RANControlRequest RANControlRequest;
typedef struct _RANMessage RANMessage;
typedef struct _UeInfoM UeInfoM;
typedef struct _UeListM UeListM;


/* --- enums --- */

typedef enum _RANMessageType {
  RAN_MESSAGE_TYPE__SUBSCRIPTION = 1,
  RAN_MESSAGE_TYPE__INDICATION_REQUEST = 2,
  RAN_MESSAGE_TYPE__INDICATION_RESPONSE = 3,
  RAN_MESSAGE_TYPE__CONTROL = 4
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(RAN_MESSAGE_TYPE)
} RANMessageType;
typedef enum _RANParameter {
  RAN_PARAMETER__GNB_ID = 1,
  RAN_PARAMETER__UE_LIST = 3
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(RAN_PARAMETER)
} RANParameter;

/* --- messages --- */

typedef enum {
  RAN_PARAM_MAP_ENTRY__VALUE__NOT_SET = 0,
  RAN_PARAM_MAP_ENTRY__VALUE_INT64_VALUE = 2,
  RAN_PARAM_MAP_ENTRY__VALUE_STRING_VALUE = 3,
  RAN_PARAM_MAP_ENTRY__VALUE_UE_LIST = 4
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(RAN_PARAM_MAP_ENTRY__VALUE)
} RANParamMapEntry__ValueCase;

struct  _RANParamMapEntry
{
  ProtobufCMessage base;
  RANParameter key;
  RANParamMapEntry__ValueCase value_case;
  union {
    int64_t int64_value;
    char *string_value;
    UeListM *ue_list;
  };
};
#define RAN_PARAM_MAP_ENTRY__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&ran_param_map_entry__descriptor) \
    , RAN_PARAMETER__GNB_ID, RAN_PARAM_MAP_ENTRY__VALUE__NOT_SET, {0} }


/*
 * RAN SUBMESSAGES 
 */
struct  _RANIndicationRequest
{
  ProtobufCMessage base;
  size_t n_target_params;
  RANParameter *target_params;
};
#define RAN_INDICATION_REQUEST__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&ran_indication_request__descriptor) \
    , 0,NULL }


struct  _RANIndicationResponse
{
  ProtobufCMessage base;
  size_t n_param_map;
  RANParamMapEntry **param_map;
  size_t n_ue_info;
  UeInfoM **ue_info;
};
#define RAN_INDICATION_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&ran_indication_response__descriptor) \
    , 0,NULL, 0,NULL }


struct  _RANControlRequest
{
  ProtobufCMessage base;
  size_t n_target_param_map;
  RANParamMapEntry **target_param_map;
};
#define RAN_CONTROL_REQUEST__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&ran_control_request__descriptor) \
    , 0,NULL }


typedef enum {
  RAN_MESSAGE__PAYLOAD__NOT_SET = 0,
  RAN_MESSAGE__PAYLOAD_RAN_INDICATION_REQUEST = 2,
  RAN_MESSAGE__PAYLOAD_RAN_INDICATION_RESPONSE = 3,
  RAN_MESSAGE__PAYLOAD_RAN_CONTROL_REQUEST = 4
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(RAN_MESSAGE__PAYLOAD)
} RANMessage__PayloadCase;

struct  _RANMessage
{
  ProtobufCMessage base;
  RANMessageType msg_type;
  RANMessage__PayloadCase payload_case;
  union {
    RANIndicationRequest *ran_indication_request;
    RANIndicationResponse *ran_indication_response;
    RANControlRequest *ran_control_request;
  };
};
#define RAN_MESSAGE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&ran_message__descriptor) \
    , RAN_MESSAGE_TYPE__SUBSCRIPTION, RAN_MESSAGE__PAYLOAD__NOT_SET, {0} }


struct  _UeInfoM
{
  ProtobufCMessage base;
  /*
   * this is to identify the ue
   */
  int32_t rnti;
  protobuf_c_boolean has_ue_rsrp;
  float ue_rsrp;
  protobuf_c_boolean has_ue_ber_up;
  float ue_ber_up;
  protobuf_c_boolean has_ue_ber_down;
  float ue_ber_down;
  protobuf_c_boolean has_ue_mcs_up;
  float ue_mcs_up;
  protobuf_c_boolean has_ue_mcs_down;
  float ue_mcs_down;
};
#define UE_INFO_M__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&ue_info_m__descriptor) \
    , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }


struct  _UeListM
{
  ProtobufCMessage base;
  int32_t connected_ues;
  size_t n_ue_info;
  UeInfoM **ue_info;
  int32_t total_prbs;
  int32_t allocated_prbs;
};
#define UE_LIST_M__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&ue_list_m__descriptor) \
    , 0, 0,NULL, 0, 0 }


/* RANParamMapEntry methods */
void   ran_param_map_entry__init
                     (RANParamMapEntry         *message);
size_t ran_param_map_entry__get_packed_size
                     (const RANParamMapEntry   *message);
size_t ran_param_map_entry__pack
                     (const RANParamMapEntry   *message,
                      uint8_t             *out);
size_t ran_param_map_entry__pack_to_buffer
                     (const RANParamMapEntry   *message,
                      ProtobufCBuffer     *buffer);
RANParamMapEntry *
       ran_param_map_entry__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   ran_param_map_entry__free_unpacked
                     (RANParamMapEntry *message,
                      ProtobufCAllocator *allocator);
/* RANIndicationRequest methods */
void   ran_indication_request__init
                     (RANIndicationRequest         *message);
size_t ran_indication_request__get_packed_size
                     (const RANIndicationRequest   *message);
size_t ran_indication_request__pack
                     (const RANIndicationRequest   *message,
                      uint8_t             *out);
size_t ran_indication_request__pack_to_buffer
                     (const RANIndicationRequest   *message,
                      ProtobufCBuffer     *buffer);
RANIndicationRequest *
       ran_indication_request__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   ran_indication_request__free_unpacked
                     (RANIndicationRequest *message,
                      ProtobufCAllocator *allocator);
/* RANIndicationResponse methods */
void   ran_indication_response__init
                     (RANIndicationResponse         *message);
size_t ran_indication_response__get_packed_size
                     (const RANIndicationResponse   *message);
size_t ran_indication_response__pack
                     (const RANIndicationResponse   *message,
                      uint8_t             *out);
size_t ran_indication_response__pack_to_buffer
                     (const RANIndicationResponse   *message,
                      ProtobufCBuffer     *buffer);
RANIndicationResponse *
       ran_indication_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   ran_indication_response__free_unpacked
                     (RANIndicationResponse *message,
                      ProtobufCAllocator *allocator);
/* RANControlRequest methods */
void   ran_control_request__init
                     (RANControlRequest         *message);
size_t ran_control_request__get_packed_size
                     (const RANControlRequest   *message);
size_t ran_control_request__pack
                     (const RANControlRequest   *message,
                      uint8_t             *out);
size_t ran_control_request__pack_to_buffer
                     (const RANControlRequest   *message,
                      ProtobufCBuffer     *buffer);
RANControlRequest *
       ran_control_request__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   ran_control_request__free_unpacked
                     (RANControlRequest *message,
                      ProtobufCAllocator *allocator);
/* RANMessage methods */
void   ran_message__init
                     (RANMessage         *message);
size_t ran_message__get_packed_size
                     (const RANMessage   *message);
size_t ran_message__pack
                     (const RANMessage   *message,
                      uint8_t             *out);
size_t ran_message__pack_to_buffer
                     (const RANMessage   *message,
                      ProtobufCBuffer     *buffer);
RANMessage *
       ran_message__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   ran_message__free_unpacked
                     (RANMessage *message,
                      ProtobufCAllocator *allocator);
/* UeInfoM methods */
void   ue_info_m__init
                     (UeInfoM         *message);
size_t ue_info_m__get_packed_size
                     (const UeInfoM   *message);
size_t ue_info_m__pack
                     (const UeInfoM   *message,
                      uint8_t             *out);
size_t ue_info_m__pack_to_buffer
                     (const UeInfoM   *message,
                      ProtobufCBuffer     *buffer);
UeInfoM *
       ue_info_m__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   ue_info_m__free_unpacked
                     (UeInfoM *message,
                      ProtobufCAllocator *allocator);
/* UeListM methods */
void   ue_list_m__init
                     (UeListM         *message);
size_t ue_list_m__get_packed_size
                     (const UeListM   *message);
size_t ue_list_m__pack
                     (const UeListM   *message,
                      uint8_t             *out);
size_t ue_list_m__pack_to_buffer
                     (const UeListM   *message,
                      ProtobufCBuffer     *buffer);
UeListM *
       ue_list_m__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   ue_list_m__free_unpacked
                     (UeListM *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*RANParamMapEntry_Closure)
                 (const RANParamMapEntry *message,
                  void *closure_data);
typedef void (*RANIndicationRequest_Closure)
                 (const RANIndicationRequest *message,
                  void *closure_data);
typedef void (*RANIndicationResponse_Closure)
                 (const RANIndicationResponse *message,
                  void *closure_data);
typedef void (*RANControlRequest_Closure)
                 (const RANControlRequest *message,
                  void *closure_data);
typedef void (*RANMessage_Closure)
                 (const RANMessage *message,
                  void *closure_data);
typedef void (*UeInfoM_Closure)
                 (const UeInfoM *message,
                  void *closure_data);
typedef void (*UeListM_Closure)
                 (const UeListM *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCEnumDescriptor    ran_message_type__descriptor;
extern const ProtobufCEnumDescriptor    ran_parameter__descriptor;
extern const ProtobufCMessageDescriptor ran_param_map_entry__descriptor;
extern const ProtobufCMessageDescriptor ran_indication_request__descriptor;
extern const ProtobufCMessageDescriptor ran_indication_response__descriptor;
extern const ProtobufCMessageDescriptor ran_control_request__descriptor;
extern const ProtobufCMessageDescriptor ran_message__descriptor;
extern const ProtobufCMessageDescriptor ue_info_m__descriptor;
extern const ProtobufCMessageDescriptor ue_list_m__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_ran_5fmessages_2eproto__INCLUDED */

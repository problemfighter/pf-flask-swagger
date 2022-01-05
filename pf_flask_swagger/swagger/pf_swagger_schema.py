from marshmallow import Schema, fields

from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.swagger.data.swagger_constant import PFSwaggerConst
from pf_flask_swagger.swagger.data.swagger_param_def import SwaggerParamDef


class PFSwaggerSchema:
    IN_PATH = "path"
    IN_QUERY = "query"
    OBJ = "object"
    ARRAY = "array"
    JWT_SCHEME = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

    @staticmethod
    def get_url_param_schema(place, name, data_type, required=False):
        return {
            "name": name,
            "in": place,
            "schema": {
                "type": data_type
            },
            "required": required
        }

    @staticmethod
    def get_component_schemas_link(name):
        return "#/components/schemas/" + name

    @staticmethod
    def get_schema_type(many):
        schema_type = None
        if many:
            schema_type = PFSwaggerSchema.ARRAY
        return schema_type

    @staticmethod
    def get_schema_def_and_ref(ref, schema_type=None):
        schema = {"type": schema_type}
        if schema_type == PFSwaggerSchema.ARRAY:
            schema["items"] = {
                "$ref": PFSwaggerSchema.get_component_schemas_link(ref)
            }
            return schema
        return {"$ref": PFSwaggerSchema.get_component_schemas_link(ref)}

    @staticmethod
    def get_request_body(definition: SwaggerParamDef, many=False):
        schema_type = PFSwaggerSchema.get_schema_type(many)
        return {
            "required": True,
            "content": {
                definition.request_content_type: {
                    "schema": PFSwaggerSchema.get_schema_def_and_ref(definition.request_schema_key, schema_type)
                }
            }
        }

    @staticmethod
    def get_response_body(definition: SwaggerParamDef, many=False):
        schema_type = PFSwaggerSchema.get_schema_type(many)
        schema = PFSwaggerSchema.get_schema_def_and_ref(definition.response_schema_key, schema_type)

        if PFFlaskSwaggerConfig.enable_pf_api_convention:
            any_of_response = {"anyOf": []}
            if definition.response_obj:
                any_of_response["anyOf"].append(PFSwaggerSchema.get_schema_def_and_ref(definition.response_schema_key))
            if definition.pf_message_response:
                any_of_response["anyOf"].append(PFSwaggerSchema.get_schema_def_and_ref(PFSwaggerConst.MESSAGE_RESPONSE))
            if definition.pf_error_details_response:
                any_of_response["anyOf"].append(PFSwaggerSchema.get_schema_def_and_ref(PFSwaggerConst.ERROR_DETAILS_RESPONSE))
            schema = any_of_response

        return {
            definition.http_response_code: {
                "content": {
                    definition.response_content_type: {
                        "schema": schema
                    }
                }
            }
        }

    @staticmethod
    def pf_api_data_schema(data, many=False):
        return Schema.from_dict({
            "data": fields.Nested(data, many=many)
        })

    @staticmethod
    def pf_api_response_base_schema_map():
        return {
            "status": fields.String(),
            "code": fields.String(),
        }

    @staticmethod
    def pf_api_response_data_schema(data, many=False, response_map=False):
        schema_map = PFSwaggerSchema.pf_api_response_base_schema_map()
        if data:
            schema_map["data"] = fields.Nested(data, many=many)
        if response_map:
            return schema_map
        return Schema.from_dict(schema_map)

    @staticmethod
    def pf_api_paginate_response_schema(data):
        schema_map = PFSwaggerSchema.pf_api_response_data_schema(data, many=True, response_map=True)
        pagination_schema = Schema.from_dict({
            "page": fields.Integer(),
            "itemPerPage": fields.Integer(),
            "total": fields.Integer(),
            "totalPage": fields.Integer(),
        })
        schema_map["pagination"] = fields.Nested(pagination_schema)
        return Schema.from_dict(schema_map)

    @staticmethod
    def pf_api_message_response_schema():
        schema_map = PFSwaggerSchema.pf_api_response_base_schema_map()
        schema_map["message"] = fields.String()
        return Schema.from_dict(schema_map)

    @staticmethod
    def pf_api_error_response_schema():
        schema_map = PFSwaggerSchema.pf_api_response_base_schema_map()
        schema_map["message"] = fields.String()
        schema_map["error"] = fields.Dict(keys=fields.String(), values=fields.String())
        return Schema.from_dict(schema_map)

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec.ext.marshmallow.field_converter import FieldConverterMixin
import pf_flask_rest_com.api_def
from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.swagger.data.swagger_constant import DataTypeConst, DefinitionTypeConst, PFSwaggerConst
from pf_flask_swagger.swagger.data.swagger_param_def import SwaggerParamDef
from pf_flask_swagger.swagger.pf_swagger_schema import PFSwaggerSchema


class PFSwaggerGenerator:
    _swagger_api_spec: APISpec = None

    def __init__(self):
        self.init_api_spec()

    def init_api_spec(self):
        FieldConverterMixin.field_mapping[pf_flask_rest_com.api_def.FileField] = ("string", "binary")
        self._swagger_api_spec = APISpec(
            title=PFFlaskSwaggerConfig.title,
            version=PFFlaskSwaggerConfig.version,
            openapi_version="3.0.2",
            plugins=[MarshmallowPlugin()]
        )
        self._init_pf_schema()

    def _add_component_schema(self, key: str, data):
        if key not in self._swagger_api_spec.components.schemas:
            self._swagger_api_spec.components.schema(key, schema=data)

    def _init_pf_schema(self):
        if PFFlaskSwaggerConfig.enable_pf_api_convention:
            self._add_component_schema(PFSwaggerConst.MESSAGE_RESPONSE, PFSwaggerSchema.pf_api_message_response_schema())
            self._add_component_schema(PFSwaggerConst.ERROR_DETAILS_RESPONSE, PFSwaggerSchema.pf_api_error_response_schema())

    def _enable_api_auth(self, definition: dict):
        if PFFlaskSwaggerConfig.enable_jwt_auth_global:
            if definition and isinstance(definition, dict):
                definition['security'] = [{"bearerAuth": []}]
                if "components" not in definition:
                    definition["components"] = {}
                definition["components"]["securitySchemes"] = {
                    "bearerAuth": {
                        "type": "http",
                        "scheme": "bearer",
                        "bearerFormat": "JWT"
                    }
                }
        return definition

    def _get_tuple_value(self, data: tuple, index: int, default=None):
        try:
            return data[index]
        except:
            return default

    def _process_get_request_parameters(self, params, parameters, place):
        if params:
            for query in params:
                if isinstance(query, tuple) and len(query) != 0:
                    name = self._get_tuple_value(query, 0)
                    data_type = self._get_tuple_value(query, 1, DataTypeConst.string)
                    is_required = self._get_tuple_value(query, 2, False)
                    parameters.append(PFSwaggerSchema.get_url_param_schema(place, name, data_type, is_required))
        return parameters

    def _get_query_and_url_parameters(self, definition: SwaggerParamDef):
        parameters = []
        self._process_get_request_parameters(definition.query_params, parameters, PFSwaggerSchema.IN_QUERY)
        self._process_get_request_parameters(definition.url_params, parameters, PFSwaggerSchema.IN_PATH)

        if parameters:
            return parameters
        return None

    def _process_and_add_request_schema(self, definition: SwaggerParamDef):
        request_schema = None
        many = False
        if definition.request_obj:
            request_schema = definition.request_obj
            if PFFlaskSwaggerConfig.enable_pf_api_convention and \
                    (definition.def_type != DefinitionTypeConst.FORM_DATA and definition.def_type != DefinitionTypeConst.FILE_UPLOAD):
                request_schema = PFSwaggerSchema.pf_api_data_schema(definition.request_obj)

        elif definition.request_list:
            request_schema = definition.request_list
            many = True
            if PFFlaskSwaggerConfig.enable_pf_api_convention:
                request_schema = PFSwaggerSchema.pf_api_data_schema(definition.request_list, many=many)

        if request_schema:
            self._add_component_schema(definition.request_schema_key, request_schema)
            return PFSwaggerSchema.get_request_body(definition, many=many)
        return None

    def _process_and_add_response_schema(self, definition: SwaggerParamDef):
        response_schema = None
        many = False
        if definition.response_obj:
            response_schema = definition.response_obj
        elif definition.response_list:
            many = True
            response_schema = definition.response_list

        if PFFlaskSwaggerConfig.enable_pf_api_convention:
            if definition.def_type == DefinitionTypeConst.PAGINATION:
                response_schema = PFSwaggerSchema.pf_api_paginate_response_schema(response_schema)
            else:
                response_schema = PFSwaggerSchema.pf_api_response_data_schema(response_schema, many=many)

        if response_schema:
            self._add_component_schema(definition.response_schema_key, response_schema)
            return PFSwaggerSchema.get_response_body(definition, many=many)
        return None

    def _get_operations(self, definition: SwaggerParamDef):
        operations = {}
        for method in definition.methods:
            request_body = self._process_and_add_request_schema(definition)
            responses = self._process_and_add_response_schema(definition)
            method = method.lower()
            operations[method] = {}
            if request_body:
                operations[method]["requestBody"] = request_body
            if responses:
                operations[method]["responses"] = responses
            if definition.tags:
                operations[method]["tags"] = definition.tags
        if operations:
            return operations
        return None

    def _entry_spec(self, definition: SwaggerParamDef):
        if definition.url:
            self._swagger_api_spec.path(
                path=definition.url,
                parameters=self._get_query_and_url_parameters(definition),
                operations=self._get_operations(definition)
            )

    def process(self, definition: SwaggerParamDef):
        definition.init_schema_key()
        self._entry_spec(definition)

    def process_list(self, definition_list: list):
        for definition in definition_list:
            self.process(definition)

    def get_swagger_spec(self):
        specification = {}
        if self._swagger_api_spec:
            specification = self._swagger_api_spec.to_dict()
            specification = self._enable_api_auth(specification)
        return specification

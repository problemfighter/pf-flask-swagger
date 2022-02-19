from functools import wraps
from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.swagger.data.swagger_constant import CommonConst, DataTypeConst, MethodConst, DefinitionTypeConst, \
    ContentTypeConst
from pf_flask_swagger.swagger.data.swagger_param_def import SwaggerParamDef


def add_swagger_endpoint(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: list = None,
        url_params: list = None, tag: str = None, method: str = None,
        def_type: str = DefinitionTypeConst.NONE, http_response_code: int = 200,
        response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        request_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False, pf_error_details_response: bool = False):
    def decorator(function):
        function.__pf_swagger__ = CommonConst.PF_SWAGGER

        @wraps(function)
        def pf_swagger_def(*args, **kwargs):
            if 'pass_definition' in kwargs and kwargs['pass_definition']:
                definition = SwaggerParamDef()
                definition.request_obj = request_obj
                definition.request_list = request_list
                definition.response_obj = response_obj
                definition.response_list = response_list
                definition.query_params = query_params
                definition.url_params = url_params
                definition.http_response_code = http_response_code
                definition.response_content_type = response_content_type
                definition.request_content_type = request_content_type
                definition.pf_error_details_response = pf_error_details_response
                definition.tag = tag
                definition.method = method
                definition.def_type = def_type
                definition.pf_message_response = pf_message_response
                return definition
            return function(*args, **kwargs)
        return pf_swagger_def
    return decorator


def get_request(
        query_params: list = None, url_params: list = None,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        response_obj=None, response_list=None,
        tag: str = None, pf_message_response: bool = False):
    return add_swagger_endpoint(
        method=MethodConst.GET, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response, http_response_code=http_response_code,
        response_content_type=response_content_type, response_obj=response_obj, response_list=response_list
    )


def post_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: list = None,
        url_params: list = None, tag: str = None,
        def_type: str = DefinitionTypeConst.NONE,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        request_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False, pf_error_details_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.POST, query_params=query_params, url_params=url_params, def_type=def_type,
        tag=tag, pf_message_response=pf_message_response, pf_error_details_response=pf_error_details_response,
        http_response_code=http_response_code, response_content_type=response_content_type, request_content_type=request_content_type
    )


def post_upload_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: list = None,
        url_params: list = None, tag: str = None,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False, pf_error_details_response: bool = False):
    return add_swagger_endpoint(
        def_type=DefinitionTypeConst.FILE_UPLOAD,
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.POST, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response,
        http_response_code=http_response_code, response_content_type=response_content_type,
        request_content_type=ContentTypeConst.MULTIPART_FORM_DATA, pf_error_details_response=pf_error_details_response
    )


def post_form_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: list = None,
        url_params: list = None, tag: str = None,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False, pf_error_details_response: bool = False):
    return add_swagger_endpoint(
        def_type=DefinitionTypeConst.FORM_DATA,
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.POST, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response,
        http_response_code=http_response_code, response_content_type=response_content_type,
        request_content_type=ContentTypeConst.FORM_DATA, pf_error_details_response=pf_error_details_response
    )


def put_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: list = None,
        url_params: list = None, tag: str = None,
        def_type: str = DefinitionTypeConst.NONE,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        request_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False, pf_error_details_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.PUT, query_params=query_params, url_params=url_params, def_type=def_type,
        tag=tag, pf_message_response=pf_message_response,
        http_response_code=http_response_code, response_content_type=response_content_type,
        request_content_type=request_content_type, pf_error_details_response=pf_error_details_response
    )


def delete_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: list = None,
        url_params: list = None, tag: str = None,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        request_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.DELETE, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response,
        http_response_code=http_response_code, response_content_type=response_content_type,
        request_content_type=request_content_type
    )


def patch_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: list = None,
        url_params: list = None, tag: str = None,
        def_type: str = DefinitionTypeConst.NONE,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        request_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False, pf_error_details_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.PATCH, query_params=query_params, url_params=url_params, def_type=def_type,
        tag=tag, pf_message_response=pf_message_response,
        http_response_code=http_response_code, response_content_type=response_content_type,
        request_content_type=request_content_type, pf_error_details_response=pf_error_details_response
    )


def get_paginate_request(
        response_obj=None, query_params: list = None,
        url_params: list = None, tag: str = None,
        pagination: bool = True, sorting: bool = True, search: bool = True,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        pf_message_response: bool = False):
    if not query_params:
        query_params = []

    if pagination:
        query_params.append((PFFlaskSwaggerConfig.get_page_param, DataTypeConst.integer))
        query_params.append((PFFlaskSwaggerConfig.item_per_page_param, DataTypeConst.integer))

    if sorting:
        query_params.append((PFFlaskSwaggerConfig.sort_field_param, DataTypeConst.string))
        query_params.append((PFFlaskSwaggerConfig.sort_order_param, DataTypeConst.string))

    if search:
        query_params.append((PFFlaskSwaggerConfig.search_field_param, DataTypeConst.string))

    return add_swagger_endpoint(
        method=MethodConst.GET, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response, response_list=response_obj,
        http_response_code=http_response_code, response_content_type=response_content_type
    )


def rest_request(
        request_obj=None, request_list=None, response_obj=None, method: str = None, response_list=None,
        query_params: list = None, url_params: list = None, tag: str = None, def_type: str = DefinitionTypeConst.NONE,
        http_response_code: int = 200, response_content_type: str = ContentTypeConst.APPLICATION_JSON,
        request_content_type: str = ContentTypeConst.APPLICATION_JSON, pf_message_response: bool = False,
        pf_error_details_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=method, query_params=query_params, url_params=url_params, def_type=def_type,
        tag=tag, pf_message_response=pf_message_response, pf_error_details_response=pf_error_details_response,
        http_response_code=http_response_code, response_content_type=response_content_type,
        request_content_type=request_content_type
    )

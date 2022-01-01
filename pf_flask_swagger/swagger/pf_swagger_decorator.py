from functools import wraps
from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.swagger.data.swagger_constant import CommonConst, MethodConst, DataType
from pf_flask_swagger.swagger.data.swagger_param_def import SwaggerParamDef


def add_swagger_endpoint(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: dict = None,
        url_params: dict = None, tag: str = None, method: str = None,
        pf_message_response: bool = False):
    def decorator(function):
        function.__pf_swagger__ = CommonConst.PF_SWAGGER

        @wraps(function)
        def pf_swagger_def(*args, **kwargs):
            if 'pfms_definition' in kwargs and kwargs['pfms_definition']:
                definition = SwaggerParamDef()
                definition.request_obj = request_obj
                definition.request_list = request_list
                definition.response_obj = response_obj
                definition.response_list = response_list
                definition.query_params = query_params
                definition.url_params = url_params
                definition.tag = tag
                definition.method = method
                definition.pf_message_response = pf_message_response
                return definition
            return function(*args, **kwargs)
        return pf_swagger_def
    return decorator


def get_request(
        query_params: dict = None, url_params: dict = None,
        tag: str = None, pf_message_response: bool = False):
    return add_swagger_endpoint(
        method=MethodConst.GET, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )


def post_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: dict = None,
        url_params: dict = None, tag: str = None,
        pf_message_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.POST, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )


def post_upload_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: dict = None,
        url_params: dict = None, tag: str = None,
        pf_message_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.POST, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )


def post_form_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: dict = None,
        url_params: dict = None, tag: str = None,
        pf_message_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.POST, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )


def put_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: dict = None,
        url_params: dict = None, tag: str = None,
        pf_message_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.PUT, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )


def delete_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: dict = None,
        url_params: dict = None, tag: str = None,
        pf_message_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.DELETE, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )


def patch_request(
        request_obj=None, request_list=None, response_obj=None,
        response_list=None, query_params: dict = None,
        url_params: dict = None, tag: str = None,
        pf_message_response: bool = False):
    return add_swagger_endpoint(
        request_obj=request_obj, request_list=request_list, response_obj=response_obj, response_list=response_list,
        method=MethodConst.PATCH, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )


def get_paginate_request(
        query_params: dict = None,
        url_params: dict = None, tag: str = None,
        pagination: bool = True, sorting: bool = True, search: bool = True,
        pf_message_response: bool = False):
    if not query_params:
        query_params = []

    if pagination:
        query_params.append((PFFlaskSwaggerConfig.get_page_param, DataType.integer))
        query_params.append((PFFlaskSwaggerConfig.item_per_page_param, DataType.integer))

    if sorting:
        query_params.append((PFFlaskSwaggerConfig.sort_field_param, DataType.string))
        query_params.append((PFFlaskSwaggerConfig.sort_order_param, DataType.string))

    if search:
        query_params.append((PFFlaskSwaggerConfig.search_field_param, DataType.string))

    return add_swagger_endpoint(
        method=MethodConst.GET, query_params=query_params, url_params=url_params,
        tag=tag, pf_message_response=pf_message_response
    )

from pf_flask_swagger.swagger.data.swagger_constant import ContentTypeConst


class SwaggerParamDef(object):
    url: str = None
    query_params: dict = None
    url_params: dict = None
    request_obj = None
    request_list = None
    response_obj = None
    response_list = None

    method: str = None
    methods: list = []
    tags: list = []
    description: str = ""
    response_content_type: str = ContentTypeConst.APPLICATION_JSON
    request_content_type: str = ContentTypeConst.APPLICATION_JSON

    pf_message_response: bool = False

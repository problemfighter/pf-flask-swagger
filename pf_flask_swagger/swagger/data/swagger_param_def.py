import random
import string

from pf_flask_swagger.swagger.data.swagger_constant import ContentTypeConst, DefinitionTypeConst


class SwaggerParamDef(object):
    url: str = None
    query_params: list = None  # list of tuple [(name, data_type, required)]
    url_params: list = None  # list of tuple [(name, data_type, required)]
    request_obj = None
    request_list = None
    response_obj = None
    response_list = None

    def_type: str = DefinitionTypeConst.NONE

    method: str = None
    tag: str = None
    methods: list = []
    tags: list = []
    description: str = ""
    response_content_type: str = ContentTypeConst.APPLICATION_JSON
    request_content_type: str = ContentTypeConst.APPLICATION_JSON

    pf_message_response: bool = False
    pf_error_details_response: bool = False

    http_response_code: int = 200

    # Only for Internal Use
    request_schema_key: str = None
    response_schema_key: str = None

    def init_schema_key(self):
        component_code = ''.join(random.choice(string.ascii_lowercase) for i in range(12))
        self.request_schema_key = "req_" + component_code
        self.response_schema_key = "res_" + component_code

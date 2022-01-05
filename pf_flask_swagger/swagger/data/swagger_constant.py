# >>>>>>>>>>>>>>>>>>>> Internal Use <<<<<<<<<<<<<<<<<

class CommonConst(object):
    PF_SWAGGER = "PF_SWAGGER"


class MethodConst(object):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class PFSwaggerConst(object):
    MESSAGE_RESPONSE = "message_response"
    ERROR_DETAILS_RESPONSE = "error_response"


class DefinitionTypeConst(object):
    NONE = None
    PAGINATION = "PAGINATION"
    FILE_UPLOAD = "FILE_UPLOAD"
    FORM_DATA = "FORM_DATA"


# >>>>>>>>>>>>>>>>>>>> External Use <<<<<<<<<<<<<<<<<

class ContentTypeConst(object):
    APPLICATION_JSON = "application/json"
    MULTIPART_FORM_DATA = "multipart/form-data"
    FORM_DATA = "application/x-www-form-urlencoded"


class DataTypeConst(object):
    integer = "integer"
    number = "number"
    string = "string"

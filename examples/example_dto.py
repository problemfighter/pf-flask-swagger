from marshmallow import fields

from pf_flask_rest_com.api_def import APIDef, FileField
from pf_flask_swagger.swagger.data.swagger_constant import DefinitionTypeConst, ContentTypeConst, DataTypeConst

query_params: list = [("age", DataTypeConst.integer, True), ("name", DataTypeConst.string)]
url_params: list = [("income", DataTypeConst.number, True), ("country", DataTypeConst.string)]


class PersonDTO(APIDef):
    first_name = fields.String(required=True, error_messages={"required": "Please enter first name"})
    last_name = fields.String(allow_none=None)
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    income = fields.Float(allow_none=None)
    image = FileField(allow_none=None)



# request_obj = None
# request_list = None
# response_obj = None
# response_list = None

tag: str = None
def_type: str = DefinitionTypeConst.NONE
http_response_code: int = 200
response_content_type: str = ContentTypeConst.APPLICATION_JSON
request_content_type: str = ContentTypeConst.APPLICATION_JSON
pf_message_response: bool = False
pf_error_details_response: bool = False

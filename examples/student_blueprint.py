from flask import Blueprint

from examples.example_dto import PersonDTO
from pf_flask_swagger.swagger.pf_swagger_decorator import rest_request

student_blueprint = Blueprint(
    name='student_blueprint',
    import_name=__name__,
    url_prefix='/student',
)


@student_blueprint.route('/create-student', methods=['DELETE'])
@rest_request(request_obj=PersonDTO, response_list=PersonDTO)
def post_request_endpoint():
    return "PF Flask Swagger Test"

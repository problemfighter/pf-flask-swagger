from flask import Flask, redirect, Blueprint
from marshmallow import fields
from pf_flask_swagger.swagger.pf_swagger_decorator import post_request, post_upload_request, rest_request
from pf_flask_swagger.flask.pf_flask_swagger import PFFlaskSwagger
from pf_flask_rest_com.api_def import FileField, APIDef


class PersonDTO(APIDef):
    first_name = fields.String(required=True, error_messages={"required": "Please enter first name"})
    last_name = fields.String(allow_none=None)
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    income = fields.Float(allow_none=None)
    image = FileField(allow_none=None)


student_blueprint = Blueprint(
    name='student_blueprint',
    import_name=__name__,
    url_prefix='/student',
)


@student_blueprint.route('/create-student', methods=['POST'])
@rest_request(request_obj=PersonDTO, response_list=PersonDTO)
def post_request_endpoint():
    return "PF Flask Swagger Test"


app = Flask(__name__)
flask_swagger = PFFlaskSwagger(app)
app.register_blueprint(student_blueprint)


@app.route('/')
def bismillah():
    return redirect("/pf-flask-swagger-ui")


@app.route('/post-request')
@post_request(request_obj=PersonDTO, response_list=PersonDTO)
def post_request_endpoint():
    return "PF Flask Swagger POST Request"


if __name__ == '__main__':
    app.run()

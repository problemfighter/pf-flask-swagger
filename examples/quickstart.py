from flask import Flask, redirect
from marshmallow import fields
from pf_flask_swagger.swagger.pf_swagger_decorator import post_request, post_upload_request
from pf_flask_swagger.flask.pf_flask_swagger import PFFlaskSwagger
from pf_flask_rest_com.api_def import FileField, APIDef

app = Flask(__name__)
flask_swagger = PFFlaskSwagger(app)


class PersonDTO(APIDef):
    first_name = fields.String(required=True, error_messages={"required": "Please enter first name"})
    last_name = fields.String(allow_none=None)
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    income = fields.Float(allow_none=None)
    image = FileField(allow_none=None)


@app.route('/')
def bismillah():
    return redirect("/pf-flask-swagger-ui")


@app.route('/post-request')
@post_request(request_obj=PersonDTO, response_list=PersonDTO)
def post_request_endpoint():
    return "PF Flask Swagger POST Request"


@app.route('/post-upload-request')
@post_upload_request(request_obj=PersonDTO)
def post_upload_request():
    return "PF Flask Swagger File Upload Request"


if __name__ == '__main__':
    app.run()

### In the name of God, the Most Gracious, the Most Merciful.

# PF-Flask-Swagger
PF Flask Swagger is created from produce Swagger API Documentation very quickly and easily.

```bash
pip install Flask
```
* Install PF Flask Swagger
```bash
pip install -U PF-Flask-Swagger
```
* Create file called *quickstart.py* and add below codes
```python
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

```

* Now run the Flask application.

<br/><br/><br/>
## Documentation
Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):
```bash
pip install -U PF-Flask-Swagger
```

**Please find [the Documentation]() with example from [hmtmcse.com]()**


<br/><br/><br/>
## Donate
[Problem Fighter](https://www.problemfighter.com/) develops and supports PF-Flask-Swagger and the libraries it uses. In order to grow
the community of contributors and users, and allow the maintainers to devote more time to the projects.


<br/><br/><br/>
## Contributing
For guidance on setting up a development environment and how to make a contribution to PF-Flask-Swagger, see the contributing guidelines.


<br/><br/><br/>
## Links
* **Changes :** [https://opensource.problemfighter.org/flask/pf-flask-swagger](https://opensource.problemfighter.org/flask/pf-flask-swagger)
* **PyPI Releases :** [https://pypi.org/project/pf-flask-swagger](https://pypi.org/project/pf-flask-swagger)
* **Source Code :** [https://github.com/problemfighter/pf-flask-swagger](https://github.com/problemfighter/pf-flask-swagger)
* **Issue Tracker :** [https://github.com/problemfighter/pf-flask-swagger/issues](https://github.com/problemfighter/pf-flask-swagger/issues)
* **Website :** [https://www.problemfighter.com/open-source](https://www.problemfighter.com/open-source)


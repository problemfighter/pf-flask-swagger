from flask import Blueprint, render_template

from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.swagger.pf_swagger_generator import PFSwaggerGenerator


class PFFlaskSwagger:
    _swagger_config = PFFlaskSwaggerConfig()
    _app = None
    _blue_print = None

    def __init__(self, app=None, swagger_config: PFFlaskSwaggerConfig = None):
        if app:
            self.init_app(app, swagger_config)

    def init_app(self, app, swagger_config: PFFlaskSwaggerConfig = None):
        self._app = app
        if swagger_config:
            self._swagger_config = swagger_config
        if self._app:
            self._init_swagger_blue_print()

    def _init_swagger_blue_print(self):
        if self._swagger_config.enable_swagger_view_page and self._app:
            blue_print = Blueprint("PFFlaskSwagger", __name__, template_folder="templates", static_folder="pf-swagger-static")
            blue_print.add_url_rule("/pf-flask-swagger-json", "pf-flask-swagger-json", self.swagger_json)
            blue_print.add_url_rule("/pf-flask-swagger-ui", "pf-flask-swagger-ui", self.swagger_ui)
            self._app.register_blueprint(blue_print)

    def swagger_json(self):
        pf_swagger_generator = PFSwaggerGenerator(self._swagger_config)
        return pf_swagger_generator.get_swagger_spec()


    def swagger_ui(self):
        return render_template('pf-swagger-ui.html')

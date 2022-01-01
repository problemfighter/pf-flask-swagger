from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig

api_spec_plugin = MarshmallowPlugin()


class PFSwaggerGenerator:
    _swagger_api_spec: APISpec = None
    _config: PFFlaskSwaggerConfig = PFFlaskSwaggerConfig()

    def __init__(self, config: PFFlaskSwaggerConfig = None):
        if config:
            self._config = config
        self.init_api_spec()

    def init_api_spec(self):
        self._swagger_api_spec = APISpec(
            title=self._config.title,
            version=self._config.version,
            openapi_version="3.0.2",
            plugins=[api_spec_plugin]
        )

    def get_swagger_spec(self):
        specification = {}
        if self._swagger_api_spec:
            specification = self._swagger_api_spec.to_dict()
        return specification

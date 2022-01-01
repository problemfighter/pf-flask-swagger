class PFFlaskSwaggerConfig(object):
    # General Config
    enable_pf_api_convention: bool = False
    enable_api_auth: bool = False

    # UI Config
    enable_swagger_view_page: bool = True
    enable_swagger_page_auth: bool = False
    swagger_page_auth_user: str = "pfadmin"
    swagger_page_auth_password: str = "pf_swagger"

    # Swagger Config
    title: str = "PF Flask Swagger"
    version: str = "1.0.0"

    # API Config
    get_page_param: str = "page"
    item_per_page_param: str = "per-page"
    sort_field_param: str = "sort-field"
    sort_order_param: str = "sort-order"
    search_field_param: str = "search"
    sort_default_order: str = "desc"
    sort_default_field: str = "id"

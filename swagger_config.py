from flasgger import Swagger

swagger_config = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'bot',
                "route": '/bot.json',
                "rule_filter": lambda rule: True,  
                "model_filter": lambda tag: True,  
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

def config_swagger(app):
    
    swagger = Swagger(app,
        template={
            "info": {
                "title": "backend api",
                "version": "1.0",
            },

        },config=swagger_config
    )

    return swagger
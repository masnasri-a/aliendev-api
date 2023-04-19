from aliendev_api.main import ApiGateway

api = ApiGateway("nasri", "Test API")
get_data = [
    [
        {
            "key": "name",
            "data_type": "string",
            "required": True
        },
        {
            "key": "age",
            "data_type": "int",
            "required": False
        }
    ]
]

api.addMethod(method="GET", prefix="/test-get",
              param_type="param", data=get_data)

api.addMethod(method="POST", prefix="/test-post", param_type="body", data=get_data)
print(api.build())

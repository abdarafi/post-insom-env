
import json

# Change to your Postman JSON Env file
json_string = """
[
                {
                        "key": "asdf",
                        "value": "asdfvalue",
                        "enabled": true
                }
]
"""

json_data = json.loads(json_string)
result_dict = {item['key']: item['value'] for item in json_data if item['enabled']}
print(result_dict)

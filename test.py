data = [
    {
        'id':author.id,
        'first_name':author.first_name,
        'last_name':author.last_name
    } for author in authors
]

## Demonstrate the serialization process without serializier
json_data = '{"first_name": "kevin", "last_name": "kenz"}'

import json
data = json.loads(json_data)
author = Author(**data)
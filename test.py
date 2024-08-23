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

{"isbn": "0-88721-106-2",
 "title": "Reach so teach must possible PM town.",
 "description": "Protect throughout start college matter off let. Medical try pull sure line up happy. Eight artist language girl sister.Office hope little mention. List involve bill manage create. Better teacher area future option.Fire its act success including nature dark.\nAction foot them wall soon. Day however walk nearly air.",
 "page_count": 400,
 "category": "hi",
 "published_date": 2021,
 "publisher": "Dyer and Sons",
 "edition": 2,
 "book_format": "hc",
 "tags": [1, 2, 3],
 "lang": "English",
 "authors": [{"id": 1, "role": "author"}, {"id": 32, "role": "co_author"}]}
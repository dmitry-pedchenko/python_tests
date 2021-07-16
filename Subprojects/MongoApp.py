# docker run --rm -p 27017:27017 mongo

from uuid import uuid4
from MongoTools import MongoTools

storage = MongoTools.get_instance()

for _ in range(2):
    dto = {
        "_id": str(uuid4()),
        "payload": f"payload: {str(uuid4())}"
    }
    storage.save_data(dto)

for data in storage.get_data():
    print(data)

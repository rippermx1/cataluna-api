import json
from firebase import Service
import uuid

service = Service()

# Read list from JSON object
with open('catalogo.json') as file:
    json_data = file.read()

items = json.loads(json_data)

# Iterate over each item and insert into Firebase database with UUID
for item in items:
    print(item)
    item['uuid'] = str(uuid.uuid4())
    service.create(item)

print("Items inserted into Firebase database.")

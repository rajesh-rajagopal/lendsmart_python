
from lendsmart_api import LendsmartClient


client = LendsmartClient("21X6U4T44Wc4UsB816")
data = {
    "account": "123456789",
    "name": "little-lotus-1245578",
    "document_name": "id.png",
    "location": "s3://purple_leaf/id.png",
    "represents_schema": "lisenceid"
}

result = client.document_create(654, data, 'This is a test')
print("client result :", result)

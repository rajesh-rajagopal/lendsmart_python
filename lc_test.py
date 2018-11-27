from lendsmart_api import LendsmartClient
from lendsmart_api.jwt.access_token.service_account import ServiceAccount

document_id = "9874563210"

service_account_key = """
"""

object_meta_data = {
 "name": "my_document",
 "account": "123456987",
 "owner_references": [{
    "kind": "Document",
    "api_version": "v1",
    "name": "driving license",
    "uid": document_id,
    "block_owner_deletion": False
}]}

data = {
    'object_meta': object_meta_data,
    'document_id': document_id,
    'prediction_name': 'welcome',
    'location': 'https://',
    'status': {'phase': 'Pending'},
}

l = LendsmartClient(ServiceAccount(service_account_key))
l.prediction.chunk_create(data)

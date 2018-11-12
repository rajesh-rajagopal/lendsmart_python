
from lendsmart_api import LendsmartClient


# PredictionChunk create data
data = {
    "object_meta": {
        "name": "myprediction",
        "account": "1111559986149859328",
        "owner_references": [
            {
                "kind": "Document",
                "api_version": "v1",
                "name": "first_document",
                "uid": "1113577918576992256",
                "block_owner_deletion": False
            }
        ]
    },
    "document_id": "1113577918576992256",
    "prediction_name": "welcome",
    "location": "https://f002.backblazeb2.com/file/rioosv2mailers/gitlab.png",
    "submitted_at":"2018-01-23T10:00:28.982993113+00:00",
    "status": {
        "phase": "Pending"
    }
}

client = LendsmartClient("21X6U4T44Wc4UsB816")
result = client.prediction.chunk_create(data)
print("client result :",result)

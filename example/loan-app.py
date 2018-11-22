
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
    "located_at": "https://f002.backblazeb2.com/file/rioosv2mailers/gitlab.png",
    "status": {
        "phase": "Pending"
    }
}

client = LendsmartClient("21X6U4T44Wc4UsB816")
result = client.prediction.loan_application_create(data)
print("client result :",result)

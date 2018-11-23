
from lendsmart_api import LendsmartClient


# PredictionWorkflow create data
data = {
   "object_meta": {
      "name": "first_workflow",
      "account": "1113566878992703488",
      "owner_references": [
         {
            "kind": "Document",
            "api_version": "v1",
            "name": "little-lotus-1245578",
            "uid": "1113577918576992256",
            "block_owner_deletion": False
         }
      ]
    },
   "document_id": "1113577918576992256",
   "mergeable": {
      "chunks": [
         "1113567011599818752_id_01.png",
         "1113567011599818752_id_02.png"
         "1113567011599818752_id_03.png",
      ]
   },
   "inference_considered_valid": "valid",
   "status": {
      "phase": "Pending"
   }
}

client = LendsmartClient("21X6U4T44Wc4UsB816")
result = client.prediction.workflow_create(data)
print("client result :", result)

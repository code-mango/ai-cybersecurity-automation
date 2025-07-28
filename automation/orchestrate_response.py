# Trigger automated containment actions
import requests

def isolate_endpoint(api_url, endpoint_id, headers):
    return requests.post(f"{api_url}/isolate", json={"id": endpoint_id}, headers=headers)

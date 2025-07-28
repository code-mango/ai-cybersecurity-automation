# Ingest logs from XDR/SIEM via API
import requests

def fetch_logs(api_url, headers):
    response = requests.get(f"{api_url}/logs", headers=headers)
    return response.json() if response.ok else []

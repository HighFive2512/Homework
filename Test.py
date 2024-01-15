import requests
import json

url = "https://highfive2512.atlassian.net/wiki/rest/api/content/98464?expand=body.view"
output_file = r"C:\temp\aaa2.txt"

headers = {
    "Authorization": "Basic aGlnaGZpdmUyNTEyQHlhaG9vLmNvbTpBVEFUVDN4RmZHRjBuWTBrSnNZb2liRHllNG54T2pzajIzaDNJT0thZEhLU212dWxzemM5T0xnY1FHbmFiV1RxMmRzSVR3SlJuX0puWG41SHlhSklPTlZUTVRKYWY1cksxTmxfeXZRRjVLdGtFSXpnVkUxTVc4VnhkZjNLZzF4MGI0YnBuTVZ4VFI2LThaSjQ4VThaMG8yN0JDLWNoUXh5dHBfUTEteURjQTRFRXVqWmd2eVFTSUk9M0VEQzNCREM=",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Perform GET request to retrieve information with ?expand=body.view
response = requests.get(url, headers=headers)
data = response.json()

# Extract and save the "body.view" value to body_content.txt file
body_content = data.get("body", {}).get("view", {}).get("value", "")
with open(output_file, "w") as file:
    file.write(body_content)

print(f"Body content saved to {output_file}")

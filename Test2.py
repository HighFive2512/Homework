import requests
import json

main_api_link = "https://highfive2512.atlassian.net/wiki/rest/api/content/98464"
body_expanded_link = "https://highfive2512.atlassian.net/wiki/rest/api/content/98464?expand=body.view"

headers = {
    "Authorization": "Basic aGlnaGZpdmUyNTEyQHlhaG9vLmNvbTpBVEFUVDN4RmZHRjBuWTBrSnNZb2liRHllNG54T2pzajIzaDNJT0thZEhLU212dWxzemM5T0xnY1FHbmFiV1RxMmRzSVR3SlJuX0puWG41SHlhSklPTlZUTVRKYWY1cksxTmxfeXZRRjVLdGtFSXpnVkUxTVc4VnhkZjNLZzF4MGI0YnBuTVZ4VFI2LThaSjQ4VThaMG8yN0JDLWNoUXh5dHBfUTEteURjQTRFRXVqWmd2eVFTSUk9M0VEQzNCREM=",
    "Accept": "application/json",
    "Content-Type": "application/json"
}


resp2 = requests.get(body_expanded_link, headers=headers)
data2 = resp2.json()
resp = requests.get(main_api_link, headers=headers)
data = resp.json()
v = data["version"]["number"]
content_upd = data2["body"]["view"]["value"]
with open(r'C:\temp\aaa.txt', 'w') as output_file:
    output_file.write(content_upd)

# with open(r'C:\temp\aaa.txt', 'r') as asd:
#     file_contnet = asd.read()
datar = {
    "version": {"number": v + 1},
    "title": "qwert2222y",
    "type": "page",
    "body": {
        "storage": {
            "value": content_upd,
            "representation": "storage"
        }
    }
}


response = requests.put(main_api_link, headers=headers, json=datar)

print(response.status_code)
print(response.text)

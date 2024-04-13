import requests

# Confluence API URL for getting and updating pages
confluence_base_url = "https://highfive2512.atlassian.net/wiki/rest/api/content"
page_id = "98464"  # Replace with the actual page ID
token = "aGlnaGZpdmUyNTEyQHlhaG9vLmNvbTpBVEFUVDN4RmZHRjBuWTBrSnNZb2liRHllNG54T2pzajIzaDNJT0thZEhLU212dWxzemM5T0xnY1FHbmFiV1RxMmRzSVR3SlJuX0puWG41SHlhSklPTlZUTVRKYWY1cksxTmxfeXZRRjVLdGtFSXpnVkUxTVc4VnhkZjNLZzF4MGI0YnBuTVZ4VFI2LThaSjQ4VThaMG8yN0JDLWNoUXh5dHBfUTEteURjQTRFRXVqWmd2eVFTSUk9M0VEQzNCREM="


def get_confluence_page(page_id):
    url = f"{confluence_base_url}/{page_id}?expand=body.view"
    headers = {"Authorization": f"Basic {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        page_data = response.json()
        print(page_data)
        if (
            "version" in page_data
            and "body" in page_data
            and "view" in page_data["body"]
        ):
            return page_data["version"]["number"], page_data["body"]["view"]["value"]
        else:
            print(f"Unexpected response format. Response: {page_data}")
            return None, None
    else:
        print(f"Failed to get page. Status code: {response.status_code}")
        return None, None


# Function to update Confluence page content
def update_confluence_page_content(page_id, current_version, new_content):
    url = f"{confluence_base_url}/{page_id}"

    # Fetch the existing content to preserve macros or custom elements
    _, existing_content = get_confluence_page(page_id)

    # Replace the existing content with the new content
    updated_content = existing_content.replace(existing_content, new_content)

    # Create a payload with the updated content
    payload = {
        "version": {"number": current_version + 1},
        "type": "page",
        "body": {"storage": {"value": updated_content, "representation": "storage"}},
    }

    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Page content updated successfully.")
    else:
        print(f"Failed to update page content. Status code: {response.status_code}")


# Get existing page version
current_version, _ = get_confluence_page(page_id)

if current_version is not None:
    # Update the content
    new_content = "asd"

    # Update the page with the new content
    update_confluence_page_content(page_id, current_version, new_content)

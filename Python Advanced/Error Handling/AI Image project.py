import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url: str) -> None:
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image


def get_image_url() -> str:
    headers = {"Authorization": "YOUR API KEY"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input.get(),
        "resolution": "256x256",
        "fallback_providers": "",
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    return result["openai"]["items"][0]["image_resource_url"]


def render_image():
    print("clicked")

    try:
        err_name.place_forget()
        image_url = get_image_url()
    except KeyError:
        err_name.place(x=175, y=50)
    else:
        display_image(image_url)


wndw = tk.Tk()
wndw.title("AI Image Generator")
wndw.geometry("500x350")

err_name = tk.Label(wndw, text="Prompt cannot be empty!", fg="red")

input = tk.Entry(wndw, width=14)
input.place(x=165, y=20)

image_label = tk.Label(wndw)
image_label.place(x=125, y=70)

generate_button = tk.Button(wndw, text="Create", height=1, command=render_image)
generate_button.place(x=300, y=18)

wndw.mainloop()

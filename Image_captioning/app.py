from flask import Flask, render_template, request, send_from_directory
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


@app.route("/", methods=["GET", "POST"])
def index():
    caption = ""
    image_filename = ""

    if request.method == "POST":
        file = request.files["image"]

        if file:
            image_filename = file.filename
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_filename)
            file.save(image_path)

            image = Image.open(image_path).convert("RGB")

            inputs = processor(images=image, return_tensors="pt")
            output = model.generate(**inputs)

            caption = processor.decode(output[0], skip_special_tokens=True)

    return render_template(
        "index.html",
        caption=caption,
        image_filename=image_filename
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
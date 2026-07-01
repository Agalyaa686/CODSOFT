# AI Image Captioning

An AI-powered web application that automatically generates descriptive captions for uploaded images using a pre-trained Transformer model from Hugging Face.

## Features

* Upload an image through a simple web interface
* Automatically generates a meaningful caption
* Powered by a pre-trained Vision-Language Transformer model
* Fast and user-friendly interface
* Built with Python and Flask

## Tech Stack

* Python
* Flask
* Transformers (Hugging Face)
* PyTorch
* Pillow (PIL)
* HTML
* CSS

## Project Structure

```
Image-Captioning/
│── app.py
│── requirements.txt
│── templates/
│   └── index.html
│── static/
│   └── style.css
│── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project folder:

   ```bash
   cd Image-Captioning
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open the local URL displayed in the terminal (for example, `http://127.0.0.1:5000`) in your browser.

## How It Works

1. Upload an image.
2. The image is processed using a pre-trained image captioning model from Hugging Face.
3. The AI analyzes the image.
4. A descriptive caption is generated and displayed on the webpage.

## Future Improvements

* Support for multiple languages
* Caption generation with confidence scores
* Voice output for generated captions
* Deploy the application online

## Author
 AGALYA
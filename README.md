# 🎨 Color Picker from Image

A simple yet powerful desktop application built with Python and Tkinter that allows users to extract the top 10 dominant colors from any image. The app uses the `colorthief` library to analyze images and display the extracted colors in both graphical and HEX code formats.

## 📸 Features

- Load and preview `.png`, `.jpg`, or any image file.
- Automatically detect and display the 10 most dominant colors in the image.
- Visual color swatches alongside their HEX codes.
- Clean and modern GUI design using Tkinter.
- Custom icons and logo support (optional).

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – for GUI
- **Pillow (PIL)** – for image handling
- **ColorThief** – for color palette extraction

## 📦 Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/color-picker-app.git
   cd color-picker-app
   ```

2. **Install dependencies:**
   ```bash
   pip install pillow colorthief
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## 🖼️ Usage

1. Click **"Select Image"** to choose a picture from your system.
2. Click **"Find Colors"** to extract and display the top 10 colors from the selected image.
3. The HEX codes of each color are shown beside colored rectangles.

## 📁 Project Structure

```
├── main.py           # Main application file
├── icon.png          # (Optional) App icon
├── logo.png          # (Optional) Logo shown in UI
├── README.md         # Project documentation
```

> **Note:** `icon.png` and `logo.png` are optional assets. If not present, the application will run without them.

## 🧠 How It Works

- Uses `ColorThief.get_palette()` to extract the 10 most prominent colors.
- Converts each RGB color to HEX format.
- Displays the colors on a dual canvas layout with corresponding HEX labels.

## 🙌 Acknowledgements

- [ColorThief](https://github.com/fengsp/color-thief-py)
- [Pillow (PIL Fork)](https://python-pillow.org/)

## 📜 License

This project is licensed under the MIT License.

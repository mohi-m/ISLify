# SignBridge

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/) [![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/mohi-m/SignBridge/pulls) [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  

**SignBridge** bridges the communication gap between spoken language and Indian Sign Language (ISL) or American Sign Language (ASL) by converting speech to ISL gestures and alphabets. It’s designed to be a powerful assistant for ISL and ASL interpretation.

## 🌟 **Features**

- **Real-time speech recognition:** Translates spoken language on the fly.
- **Speech-to-gesture conversion:** Converts recognized speech to ISL/ASL gestures (GIFs).
- **Fallback for unrecognized words:** Displays alphabet images for unmatched words.
- **User-friendly interface:** A simple and intuitive graphical interface for seamless interaction.

## 📺 **Demo**

- **Local Demo:**  
  Navigate to `SignBridge/demo/` and open [SignBridge.mp4](demo/SignBridge.mp4).

- **YouTube Demo:**  
  [Watch on YouTube](https://www.youtube.com/watch?v=FtxN6E09L_Y)

## 🗂 **Project Structure**

```plaintext
SignBridge/
├── resources/
│   ├── isl_gifs/               # ISL gesture GIFs
│   ├── asl_gifs/               # ASL gesture GIFs
│   ├── letters/                # Alphabet images
│   ├── signlang.png            # Logo or banner
│   ├── supported_isl_phrases.json
│   └── supported_asl_phrases.json
│
├── src/
│   ├── interface/
│   │   └── gui.py              # Graphical interface logic
│   │
│   ├── processor/
│   │   ├── image_processor.py  # Image processing utilities
│   │   └── speech_processor.py # Speech recognition logic
│   │
│   ├── main.py                 # Entry point for the application
│   └── my_utils.py             # Utility functions
│
├── demo/
│   └── SignBridge.mp4          # Demo video
│
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

## 🛠 **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/mohi-m/SignBridge.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SignBridge
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 **Usage**

1. Run the application:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions:
   - Speak into your microphone to activate real-time speech recognition.
   - View corresponding ISL/ASL gestures or alphabet images for your input.

## 📋 **Dependencies**

Ensure you have the following Python packages installed (automatically installed via `requirements.txt`):

- `speech_recognition`
- `numpy`
- `easygui`
- `Pillow`
- `tkinter`

## 🤝 **Contributing**

Contributions are always welcome! Here's how you can help:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you'd like to modify.

## 📄 **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## 💬 **Feedback**

If you have any questions, suggestions, or feedback, feel free to open an issue or reach out!

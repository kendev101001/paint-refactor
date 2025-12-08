# PyQt6 Paint Application

A modern, soon to be feature-rich paint application built with PyQt6, implementing the Model-View-Controller (MVC) architecture. This project extends and improves upon the basic PyQt6 paint tutorial by [Martin Fitzpatrick]([http://example.com](https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/)), transforming a simple drawing canvas into a full-featured paint application.

## 📋 Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Improvements from Original](#improvements-from-original)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## ✨ Features

### Drawing Tools
- **Freehand Drawing** - Natural brush strokes with smooth lines
- **Shape Tools** - Draw perfect lines, rectangles, and circles
- **Live Preview** - See shapes before finalizing them
- **Adjustable Brush Size** - Slider control for brush width (1-20px)
- **Color Picker** - Full color selection dialog

### Canvas Management
- **Resizable Canvas** - Multiple aspect ratio presets (3:4, 16:9)
- **Clear Canvas** - Quick reset functionality
- **Persistent Drawing** - Canvas content preserved during resize

### User Interface
- **Intuitive Controls** - Clear button layout for all tools
- **Menu Bar** - Easy access to canvas size options
- **Real-time Feedback** - Brush size indicator

<!--
## 📸 Screenshots

*[Add screenshots of your application here]*

![Main Interface](screenshots/main-interface.png)
![Drawing Tools](screenshots/drawing-tools.png)
![Color Picker](screenshots/color-picker.png)

!-->

## 🏗️ Architecture

This application follows the **Model-View-Controller (MVC)** design pattern:

### Model
- Manages the drawing data and canvas state
- Handles tool configurations (brush size, color, tool type)
- Maintains drawing history and canvas properties

### View
- Canvas widget for displaying drawings
- UI components (buttons, sliders, menus)
- Visual feedback for user actions

### Controller
- Handles user input events (mouse movements, button clicks)
- Coordinates between Model and View
- Manages tool switching and parameter updates

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. Clone the repository:
```bash
git clone https://github.com/kendev101001/paint-refactor.git
cd pyqt6-paint-app

```

2. Create a virtual environment (recommended) (mac)
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage
Run the application:
```bash
python main.py
```

### Basic Controls
- Select Tool: Click on any tool button (Freehand, Line, Rectangle, Circle)
- Choose Colour: "Choose Colour" button opens a colour select dialogue
- Adjust Brush Size: Use the slider to choose brush size, 1-20px
- Change Canvas Size: Use menu bar "Canvas Size" options
- Clear Canvas: Click "Clear" button to reset the canvas

## Project Structure
paint-refactor/
├── main.py                 # Application entry point
├── controllers/
│   ├── __init__.py
│   └── paint_controller.py # Main controller logic
├── models/
│   ├── __init__.py
│   ├── canvas_model.py     # Canvas state and data
│   └── tool_model.py       # Tool configurations
├── views/
│   ├── __init__.py
│   ├── main_window.py      # Main application window
│   ├── canvas_widget.py    # Drawing canvas implementation
│   └── control_panel.py    # UI controls and toolbar
├── utils/
│   ├── __init__.py
│   └── constants.py        # Application constants
├── requirements.txt
└── README.md

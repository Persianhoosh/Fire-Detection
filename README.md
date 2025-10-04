# 🔥 Fire Detection with YOLOv5
A simple real-time **fire detection** system using a custom-trained **YOLOv5** model and your system’s webcam.  
This program captures video from the webcam, processes it with a trained YOLOv5 model, and highlights detected fire regions in real-time.

---
📷 Example Output
![sample](https://github.com/Persianhoosh/i-.icons/raw/main/fire-sample1.mp4)
Example of YOLOv5 detecting fire in a live webcam feed.

---

## 📌 Features
    - Uses a custom-trained YOLOv5 model (`yolov5s_best.pt`)
    - Real-time webcam image processing
    - Annotated frames with detection results
    - Fast, live inference
---

## 📂 Project Structure
    project-folder/
        │
        ├── yolov5_fire_detection.py # Main project code
        ├── yolov5s_best.pt # Trained YOLOv5 model
        └── README.md # Project documentation

## ⚙️ Requirements
Before running, ensure your Python environment is ready.

### Install Dependencies
```bash
pip install torch torchvision torchaudio
pip install opencv-python
pip install yolov5
🚀 How to Run
Place your trained model in the MODEL_PATH location.
```

### Run the main script:
    bash
      Copy code
      python yolov5_fire_detection.py
      A window will open showing the live webcam feed annotated with detection results.

Press q to exit the program.

### 🛠 Requirements
    Python 3.8+
    OpenCV
    PyTorch
    YOLOv5 trained model
---

Fallow me :
   ==============================
   [<img src="https://raw.githubusercontent.com/Persianhoosh/i-.icons/main/youtube.png" width="50">](https://youtube.com/persianhoosh)
   [<img src="https://raw.githubusercontent.com/Persianhoosh/i-.icons/main/github.png" width="50">](https://github.com/persianhoosh)
   [<img src="https://raw.githubusercontent.com/Persianhoosh/i-.icons/main/telegram.png" width="50">](https://t.me/Aihoma)
   [<img src="https://raw.githubusercontent.com/Persianhoosh/i-.icons/main/instagram.png" width="50">](https://)

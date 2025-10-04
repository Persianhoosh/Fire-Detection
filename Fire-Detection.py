
#Fallow me on:
#https://T.me/AiHoma
#https://github.com/persianhoosh
#https://medium.com/@AiHoma


import cv2
import torch


MODEL_PATH = r"C:\Users\sorou\Desktop\New folder\yolov5s_best.pt"


def main():
    model = torch.hub.load(
        'ultralytics/yolov5',
        'custom',
        path=MODEL_PATH,
        force_reload=True
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Unable to open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to capture frame.")
            break

        results = model(frame)
        annotated_frame = results.render()[0]

        cv2.imshow("🔥 Fire Detection - YOLOv5", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

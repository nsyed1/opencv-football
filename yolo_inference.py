from ultralytics import YOLO

# model = YOLO('yolov8x')
model = YOLO('models/best.pt')

# model detections are stored as objects by default 
results = model.predict('input_videos/08fd33_4.mp4', save=True)

# print results of first frame
print(results[0]) 
print("===============================")
# loop over boxes in the first frame
for box in results[0].boxes:
    print(box)

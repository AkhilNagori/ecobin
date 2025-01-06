from ultralytics import YOLO
model = YOLO('best.pt')
results = model.track(source=0, show=True, tracker="bytetrack.yaml")

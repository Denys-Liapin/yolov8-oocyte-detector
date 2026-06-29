from ultralytics import YOLO

model = YOLO('best.onnx')

results = model('oocyte_test_photo.jpg', conf=0.5)

results[0].save()
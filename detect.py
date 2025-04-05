import cv2
from ultralytics import YOLO

# yolo11x là  một model AI  có thể giúp mình xử lý hình ảnh
# Ứng dụng: giao thông, xe tự hành
model = YOLO("yolo11x.pt")

def predict(chosen_model, img, classes=[], conf=0.5):
    if classes:
        results = chosen_model.predict(img, classes=classes, conf=conf)
    else:
        results = chosen_model.predict(img, conf=conf)
    return results

def predict_and_detect(chosen_model, img, classes=[], conf=0.5, rectangle_thickness=2, text_thickness=1):
    results = predict(chosen_model, img, classes, conf=conf)
    for result in results:
        for box in result.boxes:
            cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                          (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (0, 255, 0), rectangle_thickness)
            cv2.putText(img, f"{result.names[int(box.cls[0])]}", 
                        (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10), 
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), text_thickness)
    return img, results

image = cv2.imread("traffic_in_Vietnam.jpg")  # edit line  again
result_img, _ = predict_and_detect(model, image, classes=[2,3], conf=0.1)  # detect other object by edit numberclass

cv2.imshow("Image", result_img)
cv2.imwrite("Result.png", result_img)
cv2.waitKey(0)


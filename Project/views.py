# views.py
from django.http import JsonResponse
from PIL import Image
from io import BytesIO
from yolo_bento_service import YOLOBentoService

def predict_food(request):
    # 이미지를 받아오는 로직
    image_data = request.FILES['image'].read()
    image = Image.open(BytesIO(image_data))

    # BentoML 모델 로드
    yolo_service = YOLOBentoService.load()
    yolo_model = yolo_service.artifacts.yolo

    # YOLO 모델로 음식 예측
    predictions = yolo_model.predict(image)

    # 예측 결과를 가지고 음식 이름과 위치를 추가하여 이미지 생성
    result_image = add_food_labels(image, predictions)

    # 이미지를 response로 반환
    response = HttpResponse(content_type="image/png")
    result_image.save(response, format="PNG")
    return response

def add_food_labels(image, predictions):
    # 예측 결과를 이용하여 이미지에 음식 이름 추가하는 로직
    # (여기에 해당 로직을 구현하세요)
    return modified_image

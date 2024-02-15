# pip install bentoml

import bentoml
from bentoml.frameworks.yolo import YOLOv3
import cv2
import numpy as np

# BentoService 클래스 작성
@bentoml.env(pip_dependencies=['tensorflow==2.3.1', 'numpy'])
@bentoml.artifacts([YOLOv3()])
class YOLOBentoService(bentoml.BentoService):
    pass

# 모델 및 예측 함수
@YOLOBentoService.artifacts(YOLOv3)
def load_yolo(self, artifacts):
    return artifacts[0]

@bentoml.api(input=bytes, batch=False)
def predict(self, image_bytes):
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
    result = self.artifacts.yolo.predict(image)
    return result

# BentoService 객체 생성 및 저장
yolo_service = YOLOBentoService()
yolo_service.pack('yolo', yolo_model_instance)
saved_path = yolo_service.save()

# BentoML 서버 시작
bentoml serve {saved_path}
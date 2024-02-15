# pip install bentoml

# yolo_bento_service.py
import bentoml
from bentoml.frameworks.yolo import YOLOv3

@bentoml.env(pip_dependencies=['tensorflow==2.3.1', 'numpy'])
@bentoml.artifacts([YOLOv3()])
class YOLOBentoService(bentoml.BentoService):
    pass

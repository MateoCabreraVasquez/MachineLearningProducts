from artifitial_vision.image_study import ImageStudy
from image_processing.ImageProcessig import ImageProccesing

class Control:
    def __init__(self):
       self.__azure=ImageStudy()
       self.__pdi=ImageProccesing()


    def upload_azure_images(self,root):
        self.__azure.upload_azure_images(root)

    def get_results(self,image_path):
        return self.__azure.get_results(image_path)

    def start_pdi(self,root):
        self.__pdi.StarProccesing(root)


Control()
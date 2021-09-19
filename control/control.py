#******************************************************************
#CLass created for linking the UI with the IA and the image processing
#******************************************************************
from artifitial_vision.image_study import ImageStudy
from image_processing.ImageProcessig import ImageProccesing

class Control:
    def __init__(self):
       self.__azure=ImageStudy()
       self.__pdi=ImageProccesing()

    #Function to upload the training images to azure IA
    #**ARGS: root where are the images
    def upload_azure_images(self,root):
        self.__azure.upload_azure_images(root)

    #Function analize one image at azure
    #**ARGS: root where are the images
    def get_results(self,image_path):
        return self.__azure.get_results(image_path)

    # Function to preprocess the training images
    # **ARGS: root where are the images
   ## def start_pdi(self,root):
    ##    self.__pdi.StarProccesing(root)



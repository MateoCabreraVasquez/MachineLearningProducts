#******************************************************************
#CLass created for manage all the IA issues
#******************************************************************

from artifitial_vision.repo.process_data import ProcessData
from artifitial_vision.repo.train_machine import TrainMachine
from artifitial_vision.repo.upload_images_to_azure import UploadImagesToAzureServer

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

class ImageStudy:
    #Constructor
    def __init__(self):
        #Establish the connection with  Azure
        ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
        training_key = "670b0863a32c46d3aedc770db2ccaa72"  # llave oculta del
        prediction_key = "670b0863a32c46d3aedc770db2ccaa72"
        proyect_id = "7c9c00d2-436b-4d21-9ebb-eef3fd7aea7f"

        credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
        trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
        project = trainer.get_project(proyect_id)

        #Instances of subclasses
        self.__procces_data=ProcessData(predictor)
        self.__train= TrainMachine(TrainMachine,project)
        self.__uploadImages= UploadImagesToAzureServer(trainer, project, proyect_id)

    #Trains the machine learning
    def train_azure_Machine (self):
        self.__train.start_training()

    #Upload images training to azure
    def upload_azure_images(self,path):
        self.__uploadImages.addImage(path)

    #Get the results of analizing image with azure
    def get_results(self,image_path):
        return self.__procces_data.imageAnalisis(image_path)









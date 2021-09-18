from matplotlib.image import  imread
from matplotlib.patches import Rectangle



class ProcessData():

    def __init__(self,predictor):
        self.predictor =predictor


    def imageAnalisis(self,image):
        img = imread(image)
        alto, ancho, _ = img.shape
        positions=[]
        names=[]
        aumount=[]

        with open(image, mode="rb") as test_data:
            results = self.predictor.detect_image("7c9c00d2-436b-4d21-9ebb-eef3fd7aea7f","Iteration11",  test_data)
            for prediction in results.predictions:
                if prediction.probability * 100 > 89:
                    names.append(prediction.tag_name )
                    print(
                        "\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(
                            prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top,
                            prediction.bounding_box.width, prediction.bounding_box.height))

                    rect = Rectangle((prediction.bounding_box.left * ancho,
                                      prediction.bounding_box.top * alto),
                                     prediction.bounding_box.width * ancho,
                                     prediction.bounding_box.height * alto,
                                     edgecolor="r", facecolor="none")
                    positions.append(rect)


        return [positions,names]


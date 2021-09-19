#******************************************************************
#CLass created to process the data
#******************************************************************


from matplotlib.image import  imread
from matplotlib.patches import Rectangle



class ProcessData():

    def __init__(self,predictor):
        self.predictor =predictor

    #function to upload one image to  azzure and process it
    #**ARGS image: the image path
    #**RETURN list with the  found images and list with the location

    def imageAnalisis(self,image):
        img = imread(image)
        alto, ancho, _ = img.shape  #Get the image dimentions
        positions=[]                #locations for the found elements
        names=[]                    #found name elements

        with open(image, mode="rb") as test_data:
            results = self.predictor.detect_image("7c9c00d2-436b-4d21-9ebb-eef3fd7aea7f","Iteration11",  test_data)
            for prediction in results.predictions:
                if prediction.probability * 100 > 89:     #treshold umbral
                    names.append(prediction.tag_name )    #add image to the list
                    print(
                        "\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(
                            prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top,
                            prediction.bounding_box.width, prediction.bounding_box.height))

                    rect = Rectangle((prediction.bounding_box.left * ancho, #Rectangle cration
                                      prediction.bounding_box.top * alto),
                                     prediction.bounding_box.width * ancho,
                                     prediction.bounding_box.height * alto,
                                     edgecolor="r", facecolor="none")
                    positions.append(rect) #rectangles add to list


        return [positions,names]


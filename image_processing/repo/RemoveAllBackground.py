from PIL import ImageFile

class RemoveAllBackground:

    def __init__(self):
        ImageFile.LOAD_TRUNCATED_IMAGES = True

'''
    def startProccesWith(self, imageList):

        for imageItem in imageList:
            f = np.fromfile(imageItem.image)
           result = remove(imageItem.image)
            imageItem.setResultImage( Image.open(io.BytesIO(result)))

'''

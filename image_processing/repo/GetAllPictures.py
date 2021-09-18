import os
from os import walk
import numpy as np

from image_processing.repo.ImageData import ImageData


class GetAllPictures:

    def startProcess(self,rootFolder):
        productsFolders = [item for item in os.listdir(rootFolder) if os.path.isdir(os.path.join(rootFolder, item))]
        listImages=[]

        for label in productsFolders:
             imagesNames = next(walk(rootFolder+"/"+label), (None, None, []))[2]

             for imageName in imagesNames:
                 fullPath=rootFolder + "/" + label+"/"+imageName
                 listImages.append(ImageData(rootFolder,imageName.replace(".jpg", ""),label,np.fromfile(fullPath)))

        return listImages


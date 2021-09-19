#******************************************************************
#CLass created to mange image PDI
#******************************************************************

from image_processing.repo.GetAllPictures import GetAllPictures
from image_processing.repo.RemoveAllBackground import RemoveAllBackground
from image_processing.repo.SaveAllPictures import SaveAllPictures


class ImageProccesing:
    def __init__(self):
        #Instances
        self.getAllPictures = GetAllPictures()          #to get all images in a path
        self.RemoveBackground = RemoveAllBackground()   #proccessing data
        self.SaveAllPictures = SaveAllPictures()        #save processed pictures

    def StarProccesing(self,root):
        listPictures=self.getAllPictures.startProcess(root)
        #self.RemoveBackground.startProccesWith(listPictures)
        self.SaveAllPictures.startProcess(root,listPictures)







from image_processing.repo.GetAllPictures import GetAllPictures
from image_processing.repo.RemoveAllBackground import RemoveAllBackground
from image_processing.repo.SaveAllPictures import SaveAllPictures


class ImageProccesing:
    def __init__(self):
        self.getAllPictures = GetAllPictures()
        self.RemoveBackground = RemoveAllBackground()
        self.SaveAllPictures = SaveAllPictures()

    def StarProccesing(self,root):
        listPictures=self.getAllPictures.startProcess(root)
        #self.RemoveBackground.startProccesWith(listPictures)
        self.SaveAllPictures.startProcess(root,listPictures)






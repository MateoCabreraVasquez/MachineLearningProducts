import os



class SaveAllPictures:

    def __init__(self):
        self.folderResultName="_____OUTPUT IMAGES____"

    def startProcess(self,root,listPictures):
        if not os.path.exists(os.path.join(root,self.folderResultName)):
             os.mkdir(os.path.join(root,self.folderResultName))

        for picture in listPictures:
            if not os.path.exists(os.path.join(root, self.folderResultName,picture.label)):
                os.mkdir(os.path.join(root, self.folderResultName,picture.label))
            picture.resultImage.save(root+"/"+self.folderResultName+"/"+picture.label +"/"+picture.name+".png")







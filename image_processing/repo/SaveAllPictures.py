#******************************************************************
#CLass created to save the images
#******************************************************************
import os
class SaveAllPictures:

    def __init__(self):
        self.folderResultName="_____OUTPUT IMAGES____"

    #Create a new folder and save into it the new images
    def startProcess(self,root,listPictures):
        if not os.path.exists(os.path.join(root,self.folderResultName)): #if the folder not exists then create it
             os.mkdir(os.path.join(root,self.folderResultName))

        for picture in listPictures:   #create new folder and save the new images
            if not os.path.exists(os.path.join(root, self.folderResultName,picture.label)):
                os.mkdir(os.path.join(root, self.folderResultName,picture.label))
            picture.resultImage.save(root+"/"+self.folderResultName+"/"+picture.label +"/"+picture.name+".png")







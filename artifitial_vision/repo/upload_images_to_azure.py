from os import walk
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region


class UploadImagesToAzureServer:


    #proyect_id azure

    def __init__(self, trainer, project, project_id):
        self.trainer = trainer
        self.project = project
        self.proyect_id = project_id


    def addImage(self, path):
        image_list = []
        _, folders, _ = next(walk(path))
        for label in folders:
            tag = self.trainer.create_tag(self.proyect_id, label)
            _, _, filenames = next(walk((path+"/")+label))
            for i in range (0,len(filenames)):
                with open((path+"/"+label+"/"+filenames[i]), "rb") as image_contents:
                    image_list.append(ImageFileCreateEntry(name=filenames[i], contents=image_contents.read(), tag_ids=[tag.id]))
                    if len(image_list)==64 or i==len(filenames)-1:
                        upload_result = self.trainer.create_images_from_files(self.project.id, ImageFileCreateBatch(images=image_list))
                        image_list.clear()
                        if not upload_result.is_batch_successful:
                            print("Image batch upload failed.")
                            for image in upload_result.images:
                                print("Image status: ", image.status)
                            exit(-1)



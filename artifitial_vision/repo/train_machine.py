#******************************************************************
#CLass created to train the machine learning
#******************************************************************

import time
class TrainMachine:
    def __init__(self,trainer,project):
        self.trainer = trainer
        self.project = project


    #gives the instrucction to azure for starting the training process
    def start_training(self):
        print ("Training...")
        iteration = self.trainer.train_project(self.project.id) #creates one iteration
        while (iteration.status != "Completed"):
            iteration = self.trainer.get_iteration(self.project.id, iteration.id) #start the process
            print ("Training status: " + iteration.status)
            print ("Waiting 10 seconds...")
            time.sleep(10)





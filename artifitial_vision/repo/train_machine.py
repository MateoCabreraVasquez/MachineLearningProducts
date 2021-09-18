import time


class TrainMachine:

    def __init__(self,trainer,project):
        self.trainer = trainer
        self.project = project


    def start_training(self):
        print ("Training...")
        iteration = self.trainer.train_project(self.project.id)
        while (iteration.status != "Completed"):
            iteration = self.trainer.get_iteration(self.project.id, iteration.id)
            print ("Training status: " + iteration.status)
            print ("Waiting 10 seconds...")
            time.sleep(10)





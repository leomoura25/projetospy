from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id     
        
        self.execute(r'A:\Área de Trabalho\BLEACH Brave Souls - 3D Action.url')
        if not self.find( "startgame", matching=0.97, waiting_time=50000):
            self.not_found("startgame")
        self.wait(5000)
        self.click()
        if not self.find( "iniciofechar", matching=0.97, waiting_time=50000):
            self.not_found("iniciofechar")
        self.wait(5000)
        self.click()
        if not self.find( "quests", matching=0.97, waiting_time=50000):
            self.not_found("quests")
        self.wait(5000)
        self.click()
        if not self.find( "events", matching=0.97, waiting_time=50000):
            self.not_found("events")
        self.wait(5000)
        self.click()
        if not self.find( "limitedtime", matching=0.97, waiting_time=50000):
            self.not_found("limitedtime")
        self.wait(5000)
        self.click()
        if not self.find( "brawlquest", matching=0.97, waiting_time=50000):
            self.not_found("brawlquest")
        self.wait(5000)
        self.click()
        if not self.find( "brawl", matching=0.97, waiting_time=50000):
            self.not_found("brawl")
        self.wait(5000)
        self.click()
        if not self.find( "veryhard", matching=0.97, waiting_time=50000):
            self.not_found("veryhard")
        self.wait(5000)
        self.click()
        if not self.find( "prepare", matching=0.97, waiting_time=50000):
            self.not_found("prepare")
        self.wait(5000)
        self.click()
        if not self.find( "startquest", matching=0.97, waiting_time=50000):
            self.not_found("startquest")
        self.wait(5000)
        self.click()
        if not self.find( "tapscreen", matching=0.97, waiting_time=50000):
            self.not_found("tapscreen")
        self.wait(5000)
        self.click()
        if not self.find( "itensobtained", matching=0.97, waiting_time=10000):
            self.not_found("itensobtained")
        self.wait(5000)
        self.click()
        if not self.find( "resultscreen", matching=0.97, waiting_time=50000):
            self.not_found("resultscreen")
        self.wait(5000)
        self.click()
        if not self.find( "retry", matching=0.97, waiting_time=50000):
            self.not_found("retry")
        self.wait(5000)
        self.click()
        
        
        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()









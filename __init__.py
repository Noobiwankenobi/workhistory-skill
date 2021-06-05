from mycroft import MycroftSkill, intent_file_handler


class Workhistory(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('workhistory.intent')
    def handle_workhistory(self, message):
        self.speak_dialog('workhistory')


def create_skill():
    return Workhistory()


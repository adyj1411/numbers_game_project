from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout

from tutorial_questions import *
from questions import *


class HomeScreen(Screen):
    pass

class EndTutorialScreen(Screen):
    pass

class EndQuizScreen(Screen):
    def on_leave(self):
        with open('data.txt', 'a') as file:
            file.write("---------------------------------------------------\n")

class NumbersGameApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name='menu'))
        sm.add_widget(EndTutorialScreen(name='end1'))
        sm.add_widget(EndQuizScreen(name='end2'))

        sm.add_widget(TutorialQuestionOneScreen(name='tutorial1'))
        sm.add_widget(TutorialQuestionTwoScreen(name='tutorial2'))
        sm.add_widget(TutorialQuestionThreeScreen(name='tutorial3'))

        sm.add_widget(QuestionOneScreen(name='q1'))
        sm.add_widget(QuestionTwoScreen(name='q2'))
        sm.add_widget(QuestionThreeScreen(name='q3'))
        sm.add_widget(QuestionFourScreen(name='q4'))
        sm.add_widget(QuestionFiveScreen(name='q5'))
        sm.add_widget(QuestionSixScreen(name='q6'))
        sm.add_widget(QuestionSevenScreen(name='q7'))
        sm.add_widget(QuestionEightScreen(name='q8'))
        sm.add_widget(QuestionNineScreen(name='q9'))
        sm.add_widget(QuestionTenScreen(name='q10'))
        sm.add_widget(QuestionElevenScreen(name='q11'))
        sm.add_widget(QuestionTwelveScreen(name='q12'))
        sm.add_widget(QuestionThirteenScreen(name='q13'))
        sm.add_widget(QuestionFourteenScreen(name='q14'))
        return sm

if __name__ == '__main__':
    NumbersGameApp().run()
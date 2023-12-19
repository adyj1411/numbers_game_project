from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder
from kivy.clock import Clock


class QuestionScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        self.start_time = Clock.get_time()

    def four_option_proceed(self, answer, next_scr):
        elapsed_time = Clock.get_time() - self.start_time
        with open('data.txt', 'a') as file:
            file.write(str(answer) + ", " + str(elapsed_time) + "\n")
        self.manager.current = next_scr
    
    def no_pattern_proceed(self, next_scr) :
        self.four_option_proceed(-1, next_scr)  # -1 will be our placeholder answer if "No Pattern Exists" is selected.


class QuestionOneScreen(QuestionScreen):
    number_sequence = StringProperty("55, 65, 20, 45, 30, 80")
    choices = ListProperty([60, 19, 98, 37])
    next_screen = 'q2'

class QuestionTwoScreen(QuestionScreen):
    number_sequence = StringProperty("22, 19, 30, 55")
    choices = ListProperty([95, 96, 97, 98])
    next_screen = 'q3'

class QuestionThreeScreen(QuestionScreen):
    number_sequence = StringProperty("76, 66, 26, 46, 96")
    choices = ListProperty([65, 36, 91, 12])
    next_screen = 'q4'

class QuestionFourScreen(QuestionScreen):
    number_sequence = StringProperty("26, 24, 31, 25, 28, 32, 30")
    choices = ListProperty([1, 27, 43, 98])
    next_screen = 'q5'

class QuestionFiveScreen(QuestionScreen):
    number_sequence = StringProperty("32, 1, 4, 64")
    choices = ListProperty([2, 96, 20, 54])
    next_screen = 'q6'

class QuestionSixScreen(QuestionScreen):
    number_sequence = StringProperty("71, 43, 13, 97, 2")
    choices = ListProperty([3, 33, 63, 44])
    next_screen = 'q7'

class QuestionSevenScreen(QuestionScreen):
    number_sequence = StringProperty("42, 17, 79, 54, 91")
    choices = ListProperty([63, 28, 85, 12])
    next_screen = 'q8'

class QuestionEightScreen(QuestionScreen):
    number_sequence = StringProperty("55, 13, 89, 2")
    choices = ListProperty([32, 33, 34, 35])
    next_screen = 'q9'

class QuestionNineScreen(QuestionScreen):
    number_sequence = StringProperty("50, 52, 54, 56, 58")
    choices = ListProperty([63, 60, 98, 71])
    next_screen = 'q10'

class QuestionTenScreen(QuestionScreen):
    number_sequence = StringProperty("66, 91, 28, 3, 10")
    choices = ListProperty([1, 2, 4, 5])
    next_screen = 'q11'

class QuestionElevenScreen(QuestionScreen):
    number_sequence = StringProperty("1, 2, 3, 5, 8, 13")
    choices = ListProperty([20, 21, 22, 23])
    next_screen = 'q12'

class QuestionTwelveScreen(QuestionScreen):
    number_sequence = StringProperty("1, 3, 6, 10, 15, 21")
    choices = ListProperty([98, 28, 38, 48])
    next_screen = 'q13'

class QuestionThirteenScreen(QuestionScreen):
    number_sequence = StringProperty("56, 12, 89, 23, 78")
    choices = ListProperty([67, 41, 26, 9])
    next_screen = 'q14'

class QuestionFourteenScreen(QuestionScreen):
    number_sequence = StringProperty("1, 2, 4, 8, 16")
    choices = ListProperty([24, 32, 64, 96])
    next_screen = 'end2'




Builder.load_string("""
<QuestionScreen> :
    BoxLayout :
        orientation : 'vertical'
        Label :
            text : root.number_sequence
            font_name : 'fonts/display-free-tfb'
            font_size : 60
        GridLayout :
            rows : 2
            Button :
                text : str(root.choices[0])
                on_press : root.four_option_proceed(root.choices[0], root.next_screen)
            Button :
                text : str(root.choices[1])
                on_press : root.four_option_proceed(root.choices[1], root.next_screen)
            Button :
                text : str(root.choices[2])
                on_press : root.four_option_proceed(root.choices[2], root.next_screen)
            Button :
                text : str(root.choices[3])
                on_press : root.four_option_proceed(root.choices[3], root.next_screen)
                
        Button :
            text : "No Pattern Exists"
            on_press : root.no_pattern_proceed(root.next_screen)
""")
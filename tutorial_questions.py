from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder

class TutorialQuestionScreen(Screen):
    pass

class TutorialQuestionOneScreen(TutorialQuestionScreen):
    question_text = StringProperty("Welcome to the tutorial. To start off, consider the following sequence. Your goal is to click on the number \n that fits best with the numbers below. For example, in this case, all of the numbers below are even, so click on the even number.")
    number_sequence = StringProperty("4, 62, 80, 18, 34")
    choices = ListProperty([55, 19, 98, 37])
    next_screen = StringProperty("tutorial2")

class TutorialQuestionTwoScreen(TutorialQuestionScreen):
    question_text = StringProperty("Some lists are sequences instead of sets. Two of the choices below are perfect squares. \n Select the one that seems to follows 16.")
    number_sequence = StringProperty("1, 4, 9, 16")
    choices = ListProperty([79, 25, 81, 32])
    next_screen = StringProperty("tutorial3")

class TutorialQuestionThreeScreen(TutorialQuestionScreen):
    question_text = StringProperty("Sometimes, there will be no discernable pattern in the numbers. Don't just guess in \n this case. Select 'No Pattern Exists' if you don't see one.")
    number_sequence = StringProperty("43, 12, 13, 96, 2, 23, 76, 74, 100")
    choices = ListProperty([44, 45, 46, 47])
    next_screen = StringProperty("end1")

Builder.load_string("""
<TutorialQuestionScreen> :
    BoxLayout :
        orientation : 'vertical'
        Label :
            text : root.question_text
            font_size : 30
            halign : 'center'
        Label :
            text : root.number_sequence
            font_name : 'fonts/display-free-tfb'
            font_size : 60
        GridLayout :
            rows : 2
            Button :
                text : str(root.choices[0])
                on_press : root.manager.current = root.next_screen
            Button :
                text : str(root.choices[1])
                on_press : root.manager.current = root.next_screen
            Button :
                text : str(root.choices[2])
                on_press : root.manager.current = root.next_screen
            Button :
                text : str(root.choices[3])
                on_press : root.manager.current = root.next_screen
                
        Button :
            text : "No Pattern Exists"
            on_press : root.manager.current = root.next_screen
""")

"""Рассчёт суммы вложений для получения ежемесячной выручки с дивидендных выплат.
   Для визуализации использован выносной модуль kivy. """
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.clearcolor = "B8860B"
Window.size = (300, 500)
Window.minimum_width, Window.minimum_height = Window.size


class Root(BoxLayout):
    name_input = ObjectProperty()
    sum_input = ObjectProperty()
    per_input = ObjectProperty()
    result = ObjectProperty()

    def calculate(self):
        goal = self.name_input.text
        float_sum = self.sum_input.text
        float_per = self.per_input.text

        try:
            calculation = (float(float_sum) * 12) * 100 / float(float_per)
            while calculation > 0:
                answer = f"\nДля вашей цели ({goal}) с расходами в {(float(float_sum)):_.2f} рублей в месяц\n" \
                         f"при вкладе под {(float(float_per)):.2f} % вам потребуется вложить {calculation:_.2f} рублей.\n" \
                         f"Однако, учитывая инфляцию, сумму стоит увеличить на 15% до {calculation * 1.15:_.2f} рублей."
                self.result.text = answer
                break
        except ValueError:
            self.result.text = 'Для рассчёта наобходимо ввести сумму и процент вклада.'
        except ZeroDivisionError:
            self.result.text = 'Процент вклада не должен быть равен 0'
        self.name_input.text = ''
        self.sum_input.text = ''
        self.per_input.text = ''


class MyApp(App):
    def build(self):
        self.title = "Dividends For Life"
        return Root()


if __name__ == '__main__':
    MyApp().run()

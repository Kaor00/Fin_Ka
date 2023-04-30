"""Рассчёт суммы вложений для получения ежемесячной выручки с дивидендных выплат.
   Для визуализации использован простой интерфейс. Так же программа обрабатывает
                все возможные ошибки ввода и рассчёта данных"""
import easygui as gui

goal = "Для чего? "
sum_for_goal = "Укажите сумму, необходимую в месяц: "
percent = "Под какой % будете вкладывать? "

form = gui.multenterbox(
    msg=f"Введите данные для рассчёта...\nдробные числа вводите через точку",
    title=f"Сколько нужно вложить, что бы получать требуемую сумму",
    fields=[goal, sum_for_goal, percent]
)

if form is None:
    exit()

goal, sum_for_goal, percent = form[0], form[1], form[2]

try:
    calculation = (float(sum_for_goal) * 12) * 100 / float(percent)
    while calculation > 0:
        answer = f"\nДля вашей цели ({goal}) с расходами в {(float(sum_for_goal)):_.2f} рублей в месяц\n"\
                 f"при вкладе под {(float(percent)):.2f} % вам потребуется вложить {calculation:_.2f} рублей.\n"\
                 f"Однако, учитывая инфляцию, сумму стоит увеличить на 15% до {calculation*1.15:_.2f} рублей."

        gui.msgbox(msg=answer)
        break
    else:
        gui.msgbox(msg="Ошибка ввода данных", ok_button="понятно")
except ValueError:
    gui.msgbox(msg="Ошибка ввода данных", ok_button="понятно")
except ZeroDivisionError:
    gui.msgbox(msg="Ошибка ввода данных", ok_button="понятно")

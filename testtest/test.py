# Модуль теста
import beast as b
class Test:
    @staticmethod
    def test_block(us, message):
        win = None
        if us.intest == True:
            try:
                ans = int(message.text)
            except ValueError as ex:
                text = "Неверный ввод."
                with open('log.txt', 'w') as f:
                    f.write(str(ex))
                return text, win
            else:
                if ans < 1 or ans > len(b.obj_list):
                    text = 'Такой вариант отсутствует'
                    return text, win
            b.obj_list[ans - 1].score += 1
        if us.q_count > 5:
            us.intest = False
            max_ = b.obj_list[0].score
            win = b.obj_list[0]
            for i in b.obj_list:
                if i.score > max_:
                    win = i
                    max_ = i.score
            text = f'Ваше тотемное животное: {win.name}!\n'
        elif us.intest:
            text = Test.qst_block(us.q_count)
            us.q_count += 1
        return text, win


    @staticmethod
    def qst_block(qcount):
        t = f'{b.question_list[qcount]}\n Введите номер варианта ответа:\n'
        for i in b.obj_list:
            t += f'{b.obj_list.index(i) + 1}. {i.ans_list[qcount]}\n'
        return t
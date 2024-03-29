# Список животных и вопросов. Для корректной работы теста вопросов
# должно быть на 1 больше чем количества животных.
# С фантазией у меня не очень, поэтому вопросы и ответы написал так) прошу понять и простить)
obj_list = []

class Beast:
    def __init__(self, name):
        self.name = name
        self.ans_list = {}
        self.score = 0
        self.img ='res/notfound.png'
        self.descr = ''
        obj_list.append(self)

question_list = {1: 'Вопроc 1',
                 2: 'Вопроc 2',
                 3: 'Вопроc 3',
                 4: 'Вопрос 4',
                 5: 'Вопрос 5'
                 }

bear = Beast('Медоед')# номер в списке 0
bear.ans_list = {1: 'Медоед Ответ 1',
                 2: 'Медоед Ответ 2',
                 3: 'Медоед Ответ 3',
                 4: 'Медоед Ответ 4',
                 5: 'Медоед Ответ 5'
                 }
bear.img = 'res/med.png'
bear.descr = """Медоед известен своим бесстрашием при совсем небольших размерах\nСистематика\n
Русское название – Медоед, лысый барсук, ратель \n
Латинское название – Mellivora capensis \n
Английское название –  Honey badger, ratel  \n
Класс – Млекопитающие (Mammalia) \n
Отряд – Хищные (Carnivora) \n
Семейство – Куньи (Mustelidae)\n
Род - Медоеды (Mellivora)\n"""

lion = Beast('Лев')# номер в списке 1
lion.ans_list = {1: 'Лев Ответ 1',
                 2: 'Лев Ответ 2',
                 3: 'Лев Ответ 3',
                 4: 'Лев Ответ 4',
                 5: 'Лев Ответ 5'
                 }
lion.img = 'res/lion.png'
lion.descr = """Льва называют царём зверей. Он и вправду ведёт царскую жизнь —\n
основными добытчиками в прайде являются львицы, однако, первым к еде приступает самец.\n                
Систематика\n 
Русское название — Индийский (азиатский) лев\n
Латинское название — Pantera leo persica\n
Английское название — Asian lion\n
Отряд — Хищные (Carnivora)\n
Семейство — Кошачьи (Felidae)\n
Род — Крупные кошки (Panthera)"""

wolf = Beast('Волк')# номер в списке 2
wolf.ans_list = {1: 'Волк Ответ 1',
                 2: 'Волк Ответ 2',
                 3: 'Волк Ответ 4',
                 4: 'Волк Ответ 4',
                 5: 'Волк Ответ 5'
                 }
wolf.img = 'res/wolf.png'
wolf.descr = """Именно этот хищник является прародителем собак всех пород.\n
Систематика\n
Русское название — волк, серый волк, обыкновенный волк, евразийский волк и др.\n
Латинское название — Canis lupus\n
Английское название — Wolf\n
Отряд — хищные (Carnivora)\n
Семейство — псовые (Canidae)\n
Род — волк (Canis), включает ещё шакала и койота. \n
Некоторые систематики выделяют в отдельный вид собаку,\n
другие считают её подвидом волка — Canis lupus familiaris."""

snake = Beast('Змея')
snake.ans_list = {1: 'Змея Ответ 1',
                  2: 'Змея Ответ 2',
                  3: 'Змея Ответ 3',
                  4: 'Змея Ответ 4',
                  5: 'Змея Ответ 5'
                  }
snake.img = 'res/snake.png'
snake.descr = """Зелёная мамба\n
Класс:      Пресмыкающиеся\n
Отряд:     Чешуйчатые\n
Семейство:      Аспиды\n
Род: Мамбы\n
Вид: Зелёная мамба\n
Международное научное название\n
Dendroaspis viridis Hallowell, 1844\n
Ведёт как древесный, так и наземный образ жизни. Активная чаще в светлое время
суток, время от времени выползает на охоту ночью. В свободное от добывания пищи
время прячется в густой кроне, где малозаметна на фоне листвы. Очень подвижная
и быстрая змея. Контактов с человеком избегает, при встрече предпочтет спастись
бегством на дереве или в кустах. Застигнутая врасплох, ведёт себя агрессивно: 
громко шипит и делает неоднократные 
выпады в сторону пришельца, используя ядовитые зубы. """



# Создаем список пользователей чтобы хранить данные о них, так как базы данных
# мы ещё не проходили:)
usr_lst = []
id_lst = []
class User:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.score = None
        self.intest = False
        self.q_count = 1

usr_dict = {}

def create_user(id, name):
    a = len(id_lst)-1
    print(a)
    usr_lst.append(None)
    usr_lst[a] = User(id, name)

def getUser(id):
    ind = id_lst.index(id)
    us = usr_lst[ind]
    return us

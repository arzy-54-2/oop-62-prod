
class Test:
    def __init__(self, value):
        self.value  = value

    def __str__(self):
        return self.value


my_str = "My srt"
my_type = Test('My type')

# print(my_str)
# print(my_type)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    # +
    def __add__(self, other):
        return self.x == other.x

    # <
    def __lt__(self, other):
        pass
    # >
    def __gt__(self, other):
        pass
    # ==
    def __eq__(self, other):
        pass


int_1 = 2
int_2 = 4
int_new = int_1 + int_2
vector_1 = Vector(13, 14)
vector_2 = Vector(31, 41)
vector_3 = vector_1 + vector_2
# print(vector_3)


class News:

    def __call__(self, *args, **kwargs):
        print(" Call View")

    def __init__(self, title):
        self.title = title


my_news = News("Title")
# my_news()


class FileOpen:

    def __enter__(self):
        print("open file")
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Close")


# with FileOpen() as f:
#     print("Read file!!")




class MathHelper:

    @staticmethod
    def add(a , b):
        return a + b


class BankAccount:
    bank_name = "Simba"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def get_owner(self):
        return self.owner


    @classmethod
    def get_bank_name(cls):
        return cls.bank_name


    @classmethod
    def crate_obj_bank(cls, owner, balance=10000):
        return cls(owner, balance)

acc_1 = BankAccount("Ardager", 1000)
acc_2 = BankAccount.crate_obj_bank("VIP Ardager")

# print(BankAccount.get_bank_name())
# print(acc_1 .get_owner())

class UserAcc:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @full_name.setter
    def full_name(self, full_name):
        if not full_name.isalpha():
            print('Пиши буквы')
        self.first_name = full_name
    
    
    
ardager = UserAcc("Ardager", "Kartanbekov")
print(ardager.first_name)
ardager.full_name = "Ardager New name"
print(ardager.first_name)
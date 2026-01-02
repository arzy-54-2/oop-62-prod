class User:
    def __init__(self, name):
        self.name = name


user = User("Ardager")
# print(user.)
# user.name = "Oleg"
# print(user.name)

class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

class PremiumAccount(Account):

    def apply_bonus(self):
        self._balance += 100

# account = Account(1000)
# premium_acc = PremiumAccount(100)

# print(account.get_balance())
# print(premium_acc.get_balance())
# print(premium_acc.apply_bonus())
# print(premium_acc.get_balance())

class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance
        self.__password = password

    def get_balance(self, password):
        if self.__password == password:
            return self._balance
        return None

    def __generate_pass(self):
        return "generate pass"

    def reset_pass(self, old_pass):
        if self.__password == old_pass:
            self.__password = self.__generate_pass()
        return None


account = BankAccount("Ardager", "Def2638", 1000)
# print(account._BankAccount__generate_pass())

# name — можно трогать
# _name — не трогай, если не понимаешь
# __name — туда вообще не лезь


from abc import ABC, abstractmethod
#
#
# # Абстрактный класс
# class PaymentSystem(ABC):
#
#     @abstractmethod
#     def pay(self):
#         pass
#
# # pay = PaymentSystem()
#
# class Visa(PaymentSystem):
#     def pay(self):
#         return print('Visa pay')
#
# class Master(PaymentSystem):
#     def pay(self):
#         return print("Master pay")
#
# class Finic(PaymentSystem):
#     def pay(self):
#         return print("Finic pay")
#
#
# visa_pay = Visa()
# master_pay = Master()
# finic_pay = Finic()
#
#
# for i in [visa_pay, master_pay, finic_pay]:
#     i.pay()


#
# class OTPSender(ABC):
#     @abstractmethod
#     def send_otp(self):
#         pass
#
# class KG(OTPSender):
#     def send_otp(self):
#         sms = """
#             <Phone>+996779280699</Phone>
#             <Text>Ваш пароль 1111</Text>
#         """
#         return sms
# class RU(OTPSender):
#     def send_otp(self):
#         sms = {
#             "Phone": "+79652341718",
#             "text": "Ваш пароль 1111"
#         }
#         return sms
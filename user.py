class User:
    def __init__(self,name,address,mail,billing_info):
        self.name = name
        self.__address = address
        self.mail = mail
        self.__billing_info = billing_info

    def change_name(self,name):
        self.name = name

    def change_mail(self,mail):
        self.mail = mail

    def update_address(self,address):
        self.__address = address

    def update_billing_info(self,billing_info):
        self.__billing_info = billing_info





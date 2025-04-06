from models.user import User
from models.crypto import Crypto

def initialize_data():
    # Verificar se há usuários
    if not User.get_all():
        print("Nenhum usuário encontrado. Inserindo dados fictícios...")
        u1 = User(name='Felipe Vieira', password='1234')
        u2 = User(name='Pedro Henrique', password='1234')
        u3 = User(name='Victor Salles', password='1234')
        u4 = User(name='Livia Alves', password='1234')
        u5 = User(name='Letícia Helena', password='1234')
        u1.save()
        u2.save()
        u3.save()
        u4.save()
        u5.save()

    # Verificar se há criptomoedas
    if not Crypto.get_all():
        print("Nenhuma cripto encontrada. Inserindo criptos iniciais...")
        ara = Crypto(symbol='ARA', name='Arakakoin', price=100.0)
        ftc = Crypto(symbol='FTC', name='Fatecoin', price=1.0)
        pdr = Crypto(symbol='PDR', name='Pedrotoken', price=10.0)
        fel = Crypto(symbol='FEL', name='Felipherium', price=10.0)
        ara.save()
        ftc.save()
        pdr.save()
        fel.save()

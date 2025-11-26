from sitecurso import app,database
from  sitecurso.models import Usuario, Post

# with app.app_context():
#     database.create_all()

#Comandos para deletar e recriar o Banco de Dados
# with app.app_context():
#     database.drop_all()
#     database.create_all()

# Comando para verificar os usuarios no Banco de Dados
with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios)

#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.username)
#     print(meus_usuarios.senha)

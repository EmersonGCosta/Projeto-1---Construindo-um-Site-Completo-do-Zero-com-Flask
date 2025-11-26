from flask_wtf import FlaskForm
from flask_wtf.file import  FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sitecurso.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    senha = PasswordField('senha', validators =[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField(' Confirmação da senha',validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarconta=  SubmitField('criar conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email= email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado, Cadastre-se com outro email ou faça o Login')

class FormLogin (FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    senha = PasswordField('senha',validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil (FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators = [FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Excel')
    Curso_vba = BooleanField('VBA')
    curso_python = BooleanField('Python')
    curso_sql = BooleanField('SQL')
    curso_java = BooleanField('Java')
    curso_powerbi = BooleanField('Power BI')


    botao_submit_editarperfil = SubmitField('Confirmar Edição')


    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Email já cadastrado, CADASTRE OUTRO EMAIL ')

class FormCriarPost (FlaskForm):
    titulo = StringField('Titulo do Post', validators=[DataRequired(), Length(2, 60)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ProjetoIgor.models import Usuario
from flask_login import current_user

class FormCriarconta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20,)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha',)])
    botao_submit_Criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
           raise ValidationError('Email já cadastrado! Cadastre-se com outro e-mail ou faça login para continuar.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Excel')
    curso_javascript = BooleanField('Curso JavaScript')
    curso_sql = BooleanField('Curso SQL')
    curso_python = BooleanField('Curso python')
    curso_devweb = BooleanField('Desenvolvimento Web')
    botao_submit_editarperfil = SubmitField('Confirmar edição')


    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
               raise ValidationError('Já existe um usuário com esse e-mail.')
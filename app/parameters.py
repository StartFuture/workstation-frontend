import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.environ["APP_NAME"]

FLASK_ENV = os.environ["FLASK_ENV"] 
FLASK_RUN_PORT =  os.environ["FLASK_RUN_PORT"]
FLASK_DEBUG =  os.environ["FLASK_DEBUG"]
APP_SECRET_KEY =  os.environ["APP_SECRET_KEY"]

PATH_HEALTH = '/health'
PATH_PROTECTED = '/protected'

PATH_LOGIN = '/login'
PATH_SIGNUP = '/signup'
PATH_TWO_FACTOR = '/two_factor'

PATH_PASSWORD_RESET = '/password_reset'
PATH_NEW_PASSWORD = '/new_password'

PATH_UPDATE_USERNAME = "/update_username"
PATH_UPDATE_EMAIL = "/update_email"
PATH_UPDATE_CPF = "/update_cpf"
PATH_UPDATE_CELLPHONE = "/update_cellphone"

PATH_USER_INFO = '/user_info'

PATH_VERIFY_JWT_INFOS = '/verify_jwt_infos'

PATH_GET_BOX = '/box'
PATH_CONFIRM_BOX = '/box/confirm_box'

PATH_SHOW_SCHEDULE = '/meu_perfil/agendamentos'
PATH_DELETE_SCHEDULE= '/meu_perfil/deletar_agendamento'
PATH_UPDATE_SCHEDULE = '/meu_perfil/atualizar_agendamento'
PATH_CREATE_SCHEDULE = '/meu_perfil/criar_agendamento'

PATH_API_BACKEND = os.environ["HOST_BACKEND_URL"]

VALID_INPUTS_USER_EDIT = ['username','email','password','cpf_cnpj','telefone','credit_card']


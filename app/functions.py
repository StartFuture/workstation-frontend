import email.message
import smtplib

def send_email(client_email, cod):
    
    senha = "WorkStation2022"
    corpo_email = f"""
    <h1>Ola,</h1>
    <h1>Seu código de verificação é:</h1>
    <h2>{cod}</h2>
    """

    msg = email.message.Message()
    msg['Subject'] = "Código de verificação"
    msg['From'] = 'WorkStation.box.email@gmail.com'
    msg['To'] = client_email
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    if password:
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
        
def send_email_password(client_email, cod):
    
    senha = "WorkStation2022"
    corpo_email = f"""
    <h1>Olá, Mateus</h1>
    <h1>Seu código para redefinição de senha é:</h1>
    <h2>{cod}</h2>
    """

    msg = email.message.Message()
    msg['Subject'] = "Recupere sua senha"
    msg['From'] = 'WorkStation.box.email@gmail.com'
    msg['To'] = client_email
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    if password:
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
        
        
def send_email_password_box(client_email, cod):
    
    senha = "WorkStation2022"
    corpo_email = f"""
    <h1>Olá, Mateus</h1>
    <h1>Sua senha de acesso na box da Faria Limas é:</h1>
    <h2>{cod}</h2>
    <h2>Esparamos você!!!</h2>
    """

    msg = email.message.Message()
    msg['Subject'] = "Senha Box"
    msg['From'] = 'WorkStation.box.email@gmail.com'
    msg['To'] = client_email
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    if password:
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
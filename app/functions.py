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
import smtplib
import datetime
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Configuración ---
personas = [
    "Adrijan",
    "Guille",
    "Luka",
    "Marcos",
    "Mario",
    "Noah",
    "Rasmus",
    "Sanket"
]

destinatarios = [
    "adrijan.ivanusec@gmail.com",
    "guillermo.palou@irbbarcelona.org",
    "LVelimirov@gmail.com",
    "marcosmorenoaguilera@gmail.com",
    "mario.egea@irbbarcelona.org",
    "wolfordnoah@gmail.com",
    "rasmus.hag@bric.ku.dk",
    "sanket.desai@irbbarcelona.org"  
]

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def persona_de_la_semana():
    semana = datetime.date.today().isocalendar()[1]
    return personas[semana % len(personas)]


def enviar_mail(persona):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = ", ".join(destinatarios)
    msg["Subject"] = f"CAKECLUB TIME: {persona}"

    cuerpo = f"""
CAKECLUB TIME 🍰

This week's Cake will be brought on Thursday by:

👉 {persona}

Enjoy it!
"""
    msg.attach(MIMEText(cuerpo.strip(), "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)


if __name__ == "__main__":
    persona = persona_de_la_semana()
    enviar_mail(persona)

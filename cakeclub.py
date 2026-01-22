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


def persona_de_la_semana(offset=0):
    """
    offset=0 -> esta semana
    offset=1 -> semana próxima
    """
    semana = datetime.date.today().isocalendar()[1]
    indice = (semana + offset) % len(personas)
    return personas[indice]


def enviar_mail(actual, proxima):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = ", ".join(destinatarios)
    msg["Subject"] = f"CAKECLUB TIME: {actual}"

    cuerpo = f"""
CAKECLUB TIME 🍰

This week's Cake will be brought on Thursday by:
 👉 {actual}

Next week it will be:
👉 {proxima}

Enjoy it!
"""
    msg.attach(MIMEText(cuerpo.strip(), "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)


if __name__ == "__main__":
    persona_actual = persona_de_la_semana(offset=0)
    persona_proxima = persona_de_la_semana(offset=1)
    enviar_mail(persona_actual, persona_proxima)

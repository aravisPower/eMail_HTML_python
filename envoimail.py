import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

# Informations SMTP
smtp_server = "smtp.XXXX.fr"
smtp_port = 587  # Utiliser 465 pour SSL, 587 pour TLS
smtp_email = "ZZZZZ@monSMTP.fr"
smtp_password = "admin"

# Informations de l'email
from_email = "XXX@YYYY.com"
to_email = "destinataire@domaine.fr"
subject = "Lettre d'information Grey Cat Pickups"

# Créer le message
msg = MIMEMultipart("related")
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = subject

# Code HTML avec le CID pour l'image
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lettre d'information</title>
</head>
<body style="font-family: Verdana, sans-serif; background-color: #e0e6ed; color: #333333; padding: 20px;">
  <!-- En-tête avec l'image -->
  <div style="text-align: center; padding: 10px;">
    <img src="cid:image1" alt="image" style="width: 200px; height: auto;">
  </div>
  <!-- Titre de l'email -->
  <h1 style="color: #3b5479; text-align: center;">Lettre d'information</h1>
  <!-- Texte de contenu-->
  <p style="color: #333333; font-size: 14px; line-height: 1.6;">
    VVous avez Trois minutes pour changer votre id !.
  </p>
  
  <!-- Pied de page -->
  <div style="margin-top: 20px; text-align: center; font-size: 12px; color: #777777;">
    <p>© 2024. Tous droits réservés.</p>
    <p><a href="#" style="color: #3b5479; text-decoration: none;">Se désabonner</a></p>
  </div>
</body>
</html>
"""

# Attacher le contenu HTML au message
msg.attach(MIMEText(html_content, "html"))

# Ajouter l'image en utilisant un CID
with open("image.png", "rb") as img_file:
    img = MIMEImage(img_file.read())
    img.add_header("Content-ID", "<image1>")  # Le CID utilisé dans le HTML
    img.add_header("Content-Disposition", "inline", filename="image.png")
    msg.attach(img)


# Envoyer l'email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Utiliser TLS
        server.login(smtp_email, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
    print("Email envoyé avec succès.")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'email: {e}")

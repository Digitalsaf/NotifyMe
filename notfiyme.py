import sounddevice as sd

import numpy as np

import smtplib, ssl




duration = 10800  # seconds


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(
        indata) * 10  # converts the sound into integers/floats which allows me to read the sound levels
    level = []
    for _i in range(
            1024):  # adds a number to the list every time it hears a sound according the sound level between 0 and 1024
        level.append((int(volume_norm)))  # keeps adding the sound levels to the list
    avg_chunk = sum(level) / len(level)  # this sums levels and divides it by the length  //// so basically the mean
    level = [int(avg_chunk)]

    if any(x in level for x in range(1, 100)):  # if any number in level is == 1 - 100 then it's true
        print("Email sent")  # if the sound levels go pass 1 then print baby is crying
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = ""  # Enter your address
        receiver_email = ""  # Enter receiver address
        password = ("") # sender email password
        message = """\
        Subject: Baby Notify

        The baby is crying."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

            port = 465  # For SSL
            password = ("")

            # Create a secure SSL context
            context = ssl.create_default_context()
            password = ("") #sender email password
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("senderemailaddress@gmail.com", password)
                # TODO: Send email here
    else:
        print("No noise")  # So if it's silent and there's no noise then print no noise


with sd.Stream(callback=print_sound):
    sd.sleep(duration * 108000)


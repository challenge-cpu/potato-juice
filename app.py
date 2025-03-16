from flask import Flask
from threading import Thread
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """ 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Squid Game</title>
        <style>
            body {
                background-color: #1a1a1a;
                color: #00ff00;
                font-family: 'Courier New', monospace;
                text-align: center;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            h1 {
                font-size: 2.5rem;
                color: #ff0000;
                margin-bottom: 20px;
            }
            .logo {
                width: 250px;
                margin: 0 auto 20px auto;
                display: block;
            }
            .panel {
                border: 1px solid #ff0000;
                padding: 20px;
                width: 50%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #2a2a2a;
                word-wrap: break-word;
            }
            .challenge-text {
                font-size: 1.2rem;
                line-height: 1.5;
                margin-bottom: 20px;
            }
            .character {
                width: 100px;
                margin-top: 20px;
            }
            .hint {
                color: #ffff00;
                font-size: 1rem;
                margin-top: 10px;
            }
            .hack-animation {
                font-size: 1rem;
                color: #00ff00;
                margin-top: 20px;
                height: 20px;
                overflow: hidden;
            }
            @keyframes hack {
                0% { content: "Initializing..."; }
                20% { content: "Bypassing firewall..."; }
                40% { content: "Decrypting data..."; }
                60% { content: "Accessing FTP..."; }
                80% { content: "System compromised."; }
                100% { content: "Ready."; }
            }
            .hack-animation::after {
                content: "Initializing...";
                animation: hack 5s infinite steps(1);
            }
        </style>
    </head>
    <body>
        <img src="https://titanui.com/wp-content/uploads/2021/10/21/Squid-Game-Logo-Vector.jpg" class="logo">
        
        <h1>▇ Squid Games ▇</h1>
        
        <div class="panel">
            <p class="challenge-text">
                Welcome, hacker. You've entered the Squid Game Challenge. 
                Your mission: infiltrate the system and retrieve the hidden secret.
            </p>
            <img class="character" src="https://www.pngplay.com/wp-content/uploads/13/Squid-Game-Soldier-Triangle-Cartoon-PNG.png">
            <p class="hint">Hint: No locks, just a username.</p>
            <p class="hint">Connect. Extract the flag.</p>
            <div class="hack-animation"></div>
        </div>

        <audio id="bg-audio" loop>
            <source src="https://dl.prokerala.com/downloads/ringtones/files/mp3/ssstik-io-1735883903828-2-65529.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>

        <script>
            // Attempt to play audio on page load or user interaction
            window.onload = function() {
                var audio = document.getElementById("bg-audio");
                audio.play().catch(function(error) {
                    console.log("Autoplay blocked: " + error);
                    // Fallback: Play on first user interaction
                    document.body.addEventListener("click", function() {
                        audio.play();
                    }, { once: true });
                });
            };
        </script>
    </body>
    </html>
    """

# Function to start the FTP server
def start_ftp():
    os.makedirs("/tmp/ftp_root", exist_ok=True)
    
    # Create the flag file inside the FTP server directory
    with open("/tmp/ftp_root/flag.txt", "w") as f:
        f.write("CyberX{F7P_H@CKER}\n")

    authorizer = DummyAuthorizer()
    authorizer.add_anonymous("/tmp/ftp_root")  # Allow anonymous login

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()

# Run FTP server in a separate thread
ftp_thread = Thread(target=start_ftp, daemon=True)
ftp_thread.start()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
hemant@Hemants-MacBook-Air telegram-mcp % uv sync
Using CPython 3.13.15 interpreter at: /opt/homebrew/opt/python@3.13/bin/python3.13
Creating virtual environment at: .venv
Resolved 77 packages in 25ms
      Built telegram-mcp @ file:///Users/hemant/Computing/Projects/Telegram/telegram-mcp                                                                                                                                            
Prepared 61 packages in 3.04s
Installed 68 packages in 47ms
 + annotated-types==0.7.0
 + anyio==4.9.0
 + attrs==25.4.0
 + black==25.9.0
 + certifi==2025.1.31
 + cffi==2.0.0
 + cfgv==3.5.0
 + click==8.1.8
 + coverage==7.13.5
 + cryptography==45.0.7
 + distlib==0.4.0
 + dotenv==0.9.9
 + filelock==3.29.0
 + flake8==7.3.0
 + h11==0.14.0
 + httpcore==1.0.7
 + httpx==0.28.1
 + httpx-sse==0.4.0
 + identify==2.6.19
 + idna==3.10
 + iniconfig==2.3.0
 + jsonschema==4.25.1
 + jsonschema-specifications==2025.9.1
 + markdown-it-py==3.0.0
 + mccabe==0.7.0
 + mcp==1.22.0
 + mdurl==0.1.2
 + mypy-extensions==1.1.0
 + nodeenv==1.10.0
 + packaging==25.0
 + pathspec==0.12.1
 + platformdirs==4.5.0
 + pluggy==1.6.0
 + pre-commit==4.6.0
 + pyaes==1.6.1
 + pyasn1==0.6.1
 + pycodestyle==2.14.0
 + pycparser==2.23
 + pydantic==2.11.1
 + pydantic-core==2.33.0
 + pydantic-settings==2.8.1
 + pyflakes==3.4.0
 + pygments==2.19.1
 + pyjwt==2.10.1
 + pytest==9.0.2
 + pytest-asyncio==1.3.0
 + pytest-cov==7.1.0
 + python-dotenv==1.1.0
 + python-json-logger==4.0.0
 + python-multipart==0.0.20
 + pytokens==0.2.0
 + pyyaml==6.0.3
 + qrcode==8.2
 + referencing==0.37.0
 + rich==14.0.0
 + rpds-py==0.29.0
 + rsa==4.9
 + shellingham==1.5.4
 + sniffio==1.3.1
 + sse-starlette==2.2.1
 + starlette==0.46.1
 + telegram-mcp==2.0.1 (from file:///Users/hemant/Computing/Projects/Telegram/telegram-mcp)
 + telethon==1.44.0
 + typer==0.20.0
 + typing-extensions==4.13.0
 + typing-inspection==0.4.2
 + uvicorn==0.34.0
 + virtualenv==20.33.1
hemant@Hemants-MacBook-Air telegram-mcp % uv run session_string_generator.py --qr
# or for phone code login:
# uv run session_string_generator.py --phone
Error: TELEGRAM_API_ID and TELEGRAM_API_HASH must be set in .env file
Create an .env file with your credentials from https://my.telegram.org/apps
zsh: command not found: #
zsh: command not found: #
hemant@Hemants-MacBook-Air telegram-mcp % uv run session_string_generator.py --qr
# or for phone code login:
# uv run session_string_generator.py --phone

----- Telegram Session String Generator -----

This script will generate a session string for your Telegram account.
The generated session string can be added to your .env file.

Your credentials will NOT be stored on any server and are only used for local authentication.

Account label (optional, e.g. 'work', 'personal'; leave empty for default): personal_mcp

----- QR Code Login -----

█▀▀▀▀▀▀▀█▀▀▀█▀▀███▀▀█▀▀▀█▀▀▀▀▀█▀▀▀▀▀▀▀█
█ █▀▀▀█ █▄█ ▀ █ █ ▄▄▄ ██▄▄ ████ █▀▀▀█ █
█ █   █ █▄ ▄▄ ▄▀█  █▄█▀ █▀ █ ▀█ █   █ █
█ ▀▀▀▀▀ █▀█▀█▀█ ▄▀█▀▄▀▄▀█▀█ █▀█ ▀▀▀▀▀ █
█▀█▀▀█▀▀▀▄ ▄▀▄▄ ▄▀▄▄ ▀▄█▄▄▀▀█▄█▀██▀█▀▀█
██ ▄▀▀▀▀▀▀▀▀     ▄ ███▄▀██▄█▄  ▀▀█ ▄ ██
█▀▄ ▄ █▀█▀▀▀▄▄▀▀▄▀▀▄▄▀▀▀ ▄▄  █ ▀█▀    █
██▀  ▀▀▀▄ ▄▀▀▀▄ █▄▀  ██▀█▄ ▄▄▄ ▄▄ █▄ ▄█
████ ▀▀▀▀▄ ▄ ▄ █    ▄▀▄▄▄▀▀█▀██▄ █▄▀ ▄█
█ ▄ ▄ ▄▀▀███ ▄▀█▀ ▀█ ▄▄▀██▄▄ ▀ █▀▀▀ ▀ █
█▀▄▄▀▀▀▀▄ ▀▄▄▄█▄█▀▄ ▄▀▀█▄█▀▀█ ▄▄▀ ▄█ ██
█ ▀▀▄▄▀▀ ▀▀ ▄█ ▄█ ▀▄▄▄▀  ██▄█ ▄█ █▀  ██
█  ▀█▀ ▀▀▀▄▄█▄▀▀ ▄█ ▄   ▄▀ ▀▄▀▀▀▀▄▀ █ █
██ ▀▀▄█▀ █▀█▄▀▄█▀ ▀▄▀ ▄▀ ▄▀▄▄▄▀▀ ▄██▀▄█
█▄█▀▀▀▄▀▀▀▄▄█▀▄ ▀▄▀ ██ ▄▄██▄ ▀ ▀  █▀▄▀█
█▀▀▀▀▀▀▀█ █ ▀ █ ▀▀ ██▀▀█▄▄█▀█ █▀█ ▄▀ ▀█
█ █▀▀▀█ █▄ █▀▄▄▄▄▄█▀ ██ ▄██▀▄ ▀▀▀ ▄█▀██
█ █   █ █  █▀▄▀ ▄▀  ▀  ▄▀  ▀ █▄ ▀ █  ██
█ ▀▀▀▀▀ █▀▀▄▄ ▄▀▀ █▄▀▄█▀▄ ▄  ██  ▀  ▀▀█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Scan the QR code above with your Telegram app:
  Open Telegram > Settings > Devices > Link Desktop Device

Or open this link on a device where you're logged in:
  tg://login?token=AQKAbntquNy3g5rvLiwJMWCmUR1ibbnlSw4TX9ugT_Htmg

Expires at: 18:48:32
Waiting for you to scan...

QR code expired, here is a fresh one.

----- QR Code Login -----

█▀▀▀▀▀▀▀█▀▀▀▀▀█▀▀▀█▀▀█▀█▀▀██▀██▀▀▀▀▀▀▀█
█ █▀▀▀█ █  █ █▀▀█▄█▀█ ▀██▀▀██ █ █▀▀▀█ █
█ █   █ █▀▄▀ ▀ ▀▀  ▀▄▄▄▀██▄▄█ █ █   █ █
█ ▀▀▀▀▀ █▀▄▀█▀▄▀█ ▄ █▀▄▀▄ ▄▀█▀█ ▀▀▀▀▀ █
█▀██▀▀▀▀▀▀▄▀▀▀  ▄ █▀▀▀ ██▀▄ ▀▄▀██▀█▀▀▀█
█▄▄▀▄ █▀▀▀ ▄█▀▄▀██ ▀█▄▀ █▀▄█ ▀ ██▄▄█ ▀█
█ ▄ █▄ ▀▄ ▀ ▄ ▄█▄▀▄█▀█▀███▀▄ ▀█ ▀██▄█▀█
█▀▀█▄█▄▀  █▀▀ ▄    █▀█▀▀▄▀▀▄ ▄█▀█ ▀▄█▀█
█▀▀█ ▄▄▀▀ ▀█ █ ▄█▀ ▄▄ ▀█▄█▀█▄▄▄▀ ▄▀ ▄▀█
█▀ ▀▀▀ ▀█   █  ▀▀▄█ █ ▄█ ▄▀▀▀██▄ ▀ ▄▄▀█
█ █ ▄▀▀▀▄▀▄ ▄███▀▀█▄█▀███  ▀  █▀▀ ██▀ █
██▀█▄▀▄▀█ ▀▀▀▄█▄▀▀▀ ▄█▄▀ ▀█▀ ▀ █ ▄▄▀█ █
█ █▄ ▄ ▀██▀▄ ▀▀ ▄  ▀▀▄ ▄▀ █ ▄▀█   ▀▄███
█ ▀██ ▄▀█▄▀ ▀▀▄ █ ██   ▀▀▀ █▀  ▄█ ▀▀ ▀█
█ █  █ ▀▀█▄   ▀ ▄█▀██▄██▄▀██▄  ▀▀▀  ▄██
█▀▀▀▀▀▀▀█ ██▄█▄ ▀▀█▄ █▀▀▀▀███ █▀█ ▄██ █
█ █▀▀▀█ █ ▄▀ █████▄▄▀█▀ █▀    ▀▀▀  █▄▀█
█ █   █ █▄▄██▄▄ ▀ █▄▀▀██▀▄  █▄▄▄▀▀█▄ ▀█
█ ▀▀▀▀▀ █▀ ██▀▀ ▀▄▄▀▄ ██  █▄▄ █ ██ ▄▄ █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Scan the QR code above with your Telegram app:
  Open Telegram > Settings > Devices > Link Desktop Device

Or open this link on a device where you're logged in:
  tg://login?token=AQKdbntquNy3g5rvLizEG8KLc_G-60akDr3YUZGGsRya6A

Expires at: 18:49:01
Waiting for you to scan...

QR code expired, here is a fresh one.

----- QR Code Login -----

█▀▀▀▀▀▀▀█▀█████▀▀▀▀▀█▀▀▀█▀▀▀█▀█▀▀▀▀▀▀▀█
█ █▀▀▀█ █▄  █▄   █▄▄▄ ██▄▄ █▀▄█ █▀▀▀█ █
█ █   █ █▄▄▄ ▀ ▀▀▄ █▄█▀ █▀▄█▀▀█ █   █ █
█ ▀▀▀▀▀ █▀▄ █ ▄▀▄▀█▀▄▀▄▀█▀█ █▀█ ▀▀▀▀▀ █
█▀█▀▀█▀▀▀▄██ ▀█▀█▀▄▄ ▀▄█▄▄▀▀█ █▀██▀█▀▀█
█▄   ▀ ▀██ █▄ ▀▀ ▄ ███▄▀██▄█▄ ▀ ▄███ ██
█ █▄▀▄▄▀▄▄█▄ █▀ ▄█▀▄▄▀▀▀ ▄▄ ▀▄ ▀█ ▄▄  █
█▀▀▄█▄ ▀ █▄▄█▄▀█▄█▀  ██▀█▄█ ▄▄▄▄▄ █▄▀▄█
█▀█▄▄ ▀▀█▄▀▀▄▄█▀▄   ▄▀▄▄▄▀▀▄▀▀██▄▀▄▀▀▄█
█ █▄ ▀ ▀▀█▀█ ▀▄▄▀ ▀█ ▄▄▀██▄█ ▀▀▄▀▀▀█▀ █
█▄ ▄▀ ▄▀█ ▀▄▄▀▄███ ▄▄▀▀█▄█▀▀▄▀▄▄▀ ▄▀ ██
██▄█▀▀▀▀▀▀█▄█▄ ▄▄▄▀█▄▄▀  █  █ ▄▀ █▀ ▄▄█
█▄ ▀ ▀ ▀▄██  █▄▀▄▄█ ▄   ▄▀ ▀▄▀▀▀▀ ▀ ▄ █
██   ▀█▀▀█ ▄█  █▀  ▄▀ ▄▀ ▄▀▄▄▀    ▀▄▀▄█
█▄██▀█▀▀▀ █▄▀▄▄▄▀ ▀▀██ ▄▄██▄▀▀ ▀ ▀█▀▄▀█
█▀▀▀▀▀▀▀█ ▄▀▀▀ ▄ ▀ ▄█▀▀█▄  ▀█ █▀█ ▄▀▄ █
█ █▀▀▀█ █▄█▄▄██▀ ▄█▀ ██ █▄▀ ▄ ▀▀▀ ▄█▀▀█
█ █   █ █ ▄  █▄█▄▀█▄▀  ▄▀    █▄ ▀ ▄  ██
█ ▀▀▀▀▀ █▀▄▀ ▄  ▀▄▀█▀▄█▀██ ▄██▄▀ ▀  ▀▀█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Scan the QR code above with your Telegram app:
  Open Telegram > Settings > Devices > Link Desktop Device

Or open this link on a device where you're logged in:
  tg://login?token=AQK6bntquNy3g5rvLiw3RozU-3PtXKjfsNBldj3qOwGjfQ

Expires at: 18:49:30
Waiting for you to scan...

Two-factor authentication enabled. Please enter your password: 

Authentication successful!

----- Your Session String -----

1BVtsOG4BuzQC4cjZg9PgxjEnm37z0qKixA_Z32W7rRc12v5U0j0IrYaiUyd6xV7_7LQeImpr-i0jc4wAX1XDPf8SSBG-5m_fNkOUHW10sLVRsHrLzgZNansndr7SaN9xMygaeTPMq4aXs_U4v81PD5UZzbcXSjK1v9iwqPso8oxvzvdXH-IIMNeqV5dM8XRfsiDOFVQcykCarvvWG8NidID9SOQqSEXRcFZzMYhlCawhEavWop5I6BdujlZniInZKTrA79ANJoPFlmOo33K5C6bGm14nqQR5uptLVmhk1PKC353Fvfv5MKaRfYVH1lsaBr2SBkA8OrgadbAFyc5YZ4rXVIbPWEI=

Add this to your .env file as:
TELEGRAM_SESSION_STRING_PERSONAL_MCP=1BVtsOG4BuzQC4cjZg9PgxjEnm37z0qKixA_Z32W7rRc12v5U0j0IrYaiUyd6xV7_7LQeImpr-i0jc4wAX1XDPf8SSBG-5m_fNkOUHW10sLVRsHrLzgZNansndr7SaN9xMygaeTPMq4aXs_U4v81PD5UZzbcXSjK1v9iwqPso8oxvzvdXH-IIMNeqV5dM8XRfsiDOFVQcykCarvvWG8NidID9SOQqSEXRcFZzMYhlCawhEavWop5I6BdujlZniInZKTrA79ANJoPFlmOo33K5C6bGm14nqQR5uptLVmhk1PKC353Fvfv5MKaRfYVH1lsaBr2SBkA8OrgadbAFyc5YZ4rXVIbPWEI=

IMPORTANT: Keep this string private and never share it with anyone!

Would you like to automatically update your .env file with this session string? (y/N): y

.env file updated successfully!
zsh: command not found: #
zsh: command not found: #
hemant@Hemants-MacBook-Air telegram-mcp % MCP_TRANSPORT=http uv run main.py
Starting 2 Telegram client(s) (personal_mcp, default)...
[08/12/26 00:19:47] INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connecting to 149.154.167.51:443/TcpFull...                                                  mtprotosender.py:234
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
[08/12/26 00:19:49] INFO     Connection to 149.154.167.51:443/TcpFull complete!                                           mtprotosender.py:285
Error starting client: Telegram client 'default' is not authorized. Interactive phone login is disabled for the MCP server because it runs over stdio. Generate a session string with `uv run session_string_generator.py`, then set TELEGRAM_SESSION_STRING or TELEGRAM_SESSION_STRING_<LABEL> in .env. For existing file sessions, run the login outside the MCP server first.
                    INFO     Disconnecting from 91.108.56.110:443/TcpFull...                                              mtprotosender.py:325
                    INFO     Disconnecting from 149.154.167.51:443/TcpFull...                                             mtprotosender.py:325
                    INFO     Disconnection from 91.108.56.110:443/TcpFull complete!                                       mtprotosender.py:345
                    INFO     Disconnection from 149.154.167.51:443/TcpFull complete!                                      mtprotosender.py:345
hemant@Hemants-MacBook-Air telegram-mcp % MCP_TRANSPORT=http uv run main.py
Starting 2 Telegram client(s) (personal_mcp, default)...
[08/12/26 00:20:55] INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connecting to 149.154.167.51:443/TcpFull...                                                  mtprotosender.py:234
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
[08/12/26 00:20:58] INFO     Connection to 149.154.167.51:443/TcpFull complete!                                           mtprotosender.py:285
Error starting client: Telegram client 'default' is not authorized. Interactive phone login is disabled for the MCP server because it runs over stdio. Generate a session string with `uv run session_string_generator.py`, then set TELEGRAM_SESSION_STRING or TELEGRAM_SESSION_STRING_<LABEL> in .env. For existing file sessions, run the login outside the MCP server first.
[08/12/26 00:20:59] INFO     Disconnecting from 91.108.56.110:443/TcpFull...                                              mtprotosender.py:325
                    INFO     Disconnecting from 149.154.167.51:443/TcpFull...                                             mtprotosender.py:325
                    INFO     Disconnection from 91.108.56.110:443/TcpFull complete!                                       mtprotosender.py:345
                    INFO     Disconnection from 149.154.167.51:443/TcpFull complete!                                      mtprotosender.py:345
hemant@Hemants-MacBook-Air telegram-mcp % uv run session_string_generator.py --qr

----- Telegram Session String Generator -----

This script will generate a session string for your Telegram account.
The generated session string can be added to your .env file.

Your credentials will NOT be stored on any server and are only used for local authentication.

Account label (optional, e.g. 'work', 'personal'; leave empty for default): 

----- QR Code Login -----

█▀▀▀▀▀▀▀█▀▀███▀▀██▀▀▀█▀█▀▀█████▀▀▀▀▀▀▀█
█ █▀▀▀█ █    ▀ ▀▀▄▄▀█ ▀██▀▀██ █ █▀▀▀█ █
█ █   █ █▀▄████▀▄▄ █ █▄▀██▄▄█ █ █   █ █
█ ▀▀▀▀▀ █▀▄▀█▀▄ █ ▄ █ ▄▀▄ ▄▀█▀█ ▀▀▀▀▀ █
█▀██▀▀▀▀▀▀██  ▄█▀ █▀▀  ██▀  ▀ ▀██▀█▀▀▀█
█▀ ▀▀█ ▀██▀  ▄▄▄██ ▀█▄▀▄█▀▄▄ ▀ █▀▄▄  ▀█
███ ▀█ ▀▀ ▄     ▄▀▄▄▀▀▀███▀▄█ █  ▄  █▀█
█▀ ▄█ ▀▀ █▀▀▄ █  ▄ ▄ █▀▀▄██  ▄███ ▀▄▄▀█
██▄  ▄ ▀▄ ▀█▀█ ▄▄  ▄█ ▀█ ▄▀█▄▄█   ▀  ██
█▀▀█▀▀▀▀  ██ ▀▄▄▀▄█▄█  █ ▄▀▀ ▀▄█ ▀  ▄▀█
█▄ █▀▄ ▀▄ ▄▄▀█▀▄▀▀▀██▀█ █▄ ▀█▀█▀▀▀▄█▀ █
█▄ █▄█ ▀▀▄ ▀█▄ █ █▀ ▄█▄▀  ▀█ ▀ █ ▄▄▀█▀█
█▄ ████▀▀▀  ▀  █▀▀ ▀ ▄ ▄▀ ▀█▄▀█▀  ▀▄▀▀█
█  ▄█▀▄▀▀█▀▄█▄█▀█ ▄▀  ▀▀▀▀ █ ▄ ██▄▀█ ▀█
█ █▄ ▄ ▀▀▀ ▀▄▀▀▀▄▀█▄█ ▀▀▄▀██▀  ▀  ▄▄▄██
█▀▀▀▀▀▀▀█    █▀▄  █▄▀ ▀ ▀▀▄▀█ █▀█ ▄█▄ █
█ █▀▀▀█ █   █ ▀ ▄█▄▄█▄▀ ▄     ▀▀▀  █▀██
█ █   █ █▄▀▀▀▀▀▄▀ ▄▄▀▀ ▀▀▄  █▄▄▄▀▀██ ▀█
█ ▀▀▀▀▀ █▀▄▄▀  ▄▀  █▄ █▄  ██▄ █▄██▄▄▄ █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Scan the QR code above with your Telegram app:
  Open Telegram > Settings > Devices > Link Desktop Device

Or open this link on a device where you're logged in:
  tg://login?token=AQJbb3tqqM1LjGpCvxohoJ4knCk7DrYuL_8kwQhicrOfZA

Expires at: 18:52:11
Waiting for you to scan...

Two-factor authentication enabled. Please enter your password: 

Authentication successful!

----- Your Session String -----

1BVtsOG4BuxxbQ7FYa8uACX864BHB9I_SP_wi5uFp4uoHwBf-xAsnDWqrtBJIdBQKvXvVpD7UJAPJZy5kiTED3gbvXkjTEczv4Uy9gI_s6KrrUbUlAijQMfcfjWghpSI6F34R46SkPg6wtACmREQADRlt0TyRPr_paqLPi5B2e4x8WMl2n0uNwCLSbd1r2sLKvWqEp1oAu2_XALLGaY4XqrVQK9rN4iiZMmJQX-L6u0lZ-o5vVTtmZv8fgKJHqgxtMmUVdA0dcB2MqOcljOXheVL0q_b5C_t5BQgPXlMy5FrmpuXzjv3jeWH0UAfkobes8L6P1nTdOMdmovwdcDpqrddSpKw8kPE=

Add this to your .env file as:
TELEGRAM_SESSION_STRING=1BVtsOG4BuxxbQ7FYa8uACX864BHB9I_SP_wi5uFp4uoHwBf-xAsnDWqrtBJIdBQKvXvVpD7UJAPJZy5kiTED3gbvXkjTEczv4Uy9gI_s6KrrUbUlAijQMfcfjWghpSI6F34R46SkPg6wtACmREQADRlt0TyRPr_paqLPi5B2e4x8WMl2n0uNwCLSbd1r2sLKvWqEp1oAu2_XALLGaY4XqrVQK9rN4iiZMmJQX-L6u0lZ-o5vVTtmZv8fgKJHqgxtMmUVdA0dcB2MqOcljOXheVL0q_b5C_t5BQgPXlMy5FrmpuXzjv3jeWH0UAfkobes8L6P1nTdOMdmovwdcDpqrddSpKw8kPE=

IMPORTANT: Keep this string private and never share it with anyone!

Would you like to automatically update your .env file with this session string? (y/N): y

.env file updated successfully!
hemant@Hemants-MacBook-Air telegram-mcp % MCP_TRANSPORT=http uv run main.py      
Starting 2 Telegram client(s) (personal_mcp, default)...
[08/12/26 00:22:10] INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
Warming entity caches (background)...
Telegram client(s) started (personal_mcp, default). Running MCP server (http)...
INFO:     Started server process [82501]
INFO:     Waiting for application startup.
                    INFO     StreamableHTTP session manager started                                             streamable_http_manager.py:110
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8765 (Press CTRL+C to quit)
Entity caches warmed.
INFO:     127.0.0.1:54439 - "POST /mcp HTTP/1.1" 406 Not Acceptable
[08/12/26 00:24:00] INFO     Terminating session: None                                                                  streamable_http.py:648
                    ERROR    Error in message router                                                                    streamable_http.py:897
                             ╭────────────────────────── Traceback (most recent call last) ───────────────────────────╮                       
                             │ /Users/hemant/Computing/Projects/Telegram/telegram-mcp/.venv/lib/python3.13/site-packa │                       
                             │ ges/mcp/server/streamable_http.py:849 in message_router                                │                       
                             │                                                                                        │                       
                             │   846 │   │   │   # Create a message router that distributes messages to request strea │                       
                             │   847 │   │   │   async def message_router():  # pragma: no cover                      │                       
                             │   848 │   │   │   │   try:                                                             │                       
                             │ ❱ 849 │   │   │   │   │   async for session_message in write_stream_reader:            │                       
                             │   850 │   │   │   │   │   │   # Determine which request stream(s) should receive this  │                       
                             │   851 │   │   │   │   │   │   message = session_message.message                        │                       
                             │   852 │   │   │   │   │   │   target_request_id = None                                 │                       
                             │                                                                                        │                       
                             │ /Users/hemant/Computing/Projects/Telegram/telegram-mcp/.venv/lib/python3.13/site-packa │                       
                             │ ges/anyio/abc/_streams.py:35 in __anext__                                              │                       
                             │                                                                                        │                       
                             │    32 │                                                                                │                       
                             │    33 │   async def __anext__(self) -> T_co:                                           │                       
                             │    34 │   │   try:                                                                     │                       
                             │ ❱  35 │   │   │   return await self.receive()                                          │                       
                             │    36 │   │   except EndOfStream:                                                      │                       
                             │    37 │   │   │   raise StopAsyncIteration                                             │                       
                             │    38                                                                                  │                       
                             │                                                                                        │                       
                             │ /Users/hemant/Computing/Projects/Telegram/telegram-mcp/.venv/lib/python3.13/site-packa │                       
                             │ ges/anyio/streams/memory.py:111 in receive                                             │                       
                             │                                                                                        │                       
                             │   108 │   async def receive(self) -> T_co:                                             │                       
                             │   109 │   │   await checkpoint()                                                       │                       
                             │   110 │   │   try:                                                                     │                       
                             │ ❱ 111 │   │   │   return self.receive_nowait()                                         │                       
                             │   112 │   │   except WouldBlock:                                                       │                       
                             │   113 │   │   │   # Add ourselves in the queue                                         │                       
                             │   114 │   │   │   receive_event = Event()                                              │                       
                             │                                                                                        │                       
                             │ /Users/hemant/Computing/Projects/Telegram/telegram-mcp/.venv/lib/python3.13/site-packa │                       
                             │ ges/anyio/streams/memory.py:93 in receive_nowait                                       │                       
                             │                                                                                        │                       
                             │    90 │   │                                                                            │                       
                             │    91 │   │   """                                                                      │                       
                             │    92 │   │   if self._closed:                                                         │                       
                             │ ❱  93 │   │   │   raise ClosedResourceError                                            │                       
                             │    94 │   │                                                                            │                       
                             │    95 │   │   if self._state.waiting_senders:                                          │                       
                             │    96 │   │   │   # Get the item from the next sender                                  │                       
                             ╰────────────────────────────────────────────────────────────────────────────────────────╯                       
                             ClosedResourceError                                                                                              
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
[08/12/26 00:24:33] INFO     StreamableHTTP session manager shutting down                                       streamable_http_manager.py:114
INFO:     Application shutdown complete.
INFO:     Finished server process [82501]
                    INFO     Disconnecting from 91.108.56.110:443/TcpFull...                                              mtprotosender.py:325
                    INFO     Disconnecting from 91.108.56.110:443/TcpFull...                                              mtprotosender.py:325
                    INFO     Disconnection from 91.108.56.110:443/TcpFull complete!                                       mtprotosender.py:345
                    INFO     Disconnection from 91.108.56.110:443/TcpFull complete!                                       mtprotosender.py:345
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 119, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/base_events.py", line 726, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/telegram_mcp/runner.py", line 143, in _main
    await asyncio.gather(
        *(cl.disconnect() for cl in clients.values()), return_exceptions=True
    )
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/main.py", line 67, in <module>
    main()
    ~~~~^^
  File "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/telegram_mcp/runner.py", line 153, in main
    asyncio.run(_main())
    ~~~~~~~~~~~^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 196, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 124, in run
    raise KeyboardInterrupt()
KeyboardInterrupt
hemant@Hemants-MacBook-Air telegram-mcp % 
hemant@Hemants-MacBook-Air telegram-mcp % MCP_TRANSPORT=sse uv run main.py
Starting 2 Telegram client(s) (personal_mcp, default)...
[08/12/26 00:25:08] INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
Warming entity caches (background)...
Telegram client(s) started (personal_mcp, default). Running MCP server (sse)...
INFO:     Started server process [84107]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8765 (Press CTRL+C to quit)
Entity caches warmed.
INFO:     127.0.0.1:54498 - "POST /sse HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:54516 - "POST /sse HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:54530 - "POST /sse HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:54530 - "POST /sse HTTP/1.1" 405 Method Not Allowed
[08/12/26 00:32:39] INFO     Got difference for channel 2552569344 updates                                                      updates.py:474
                    INFO     Got difference for channel 2552569344 updates                                                      updates.py:474
INFO:     127.0.0.1:54772 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54772 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54790 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54790 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54816 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54816 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54877 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54877 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54877 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54877 - "GET /mcp HTTP/1.1" 404 Not Found
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [84107]
[08/12/26 00:36:14] INFO     Disconnecting from 91.108.56.110:443/TcpFull...                                              mtprotosender.py:325
                    INFO     Disconnecting from 91.108.56.110:443/TcpFull...                                              mtprotosender.py:325
                    INFO     Disconnection from 91.108.56.110:443/TcpFull complete!                                       mtprotosender.py:345
                    INFO     Disconnection from 91.108.56.110:443/TcpFull complete!                                       mtprotosender.py:345
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 119, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/base_events.py", line 726, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/telegram_mcp/runner.py", line 143, in _main
    await asyncio.gather(
        *(cl.disconnect() for cl in clients.values()), return_exceptions=True
    )
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/main.py", line 67, in <module>
    main()
    ~~~~^^
  File "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/telegram_mcp/runner.py", line 153, in main
    asyncio.run(_main())
    ~~~~~~~~~~~^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 196, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.15/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 124, in run
    raise KeyboardInterrupt()
KeyboardInterrupt
hemant@Hemants-MacBook-Air telegram-mcp % 
hemant@Hemants-MacBook-Air telegram-mcp % MCP_TRANSPORT=sse uv run main.py
Starting 2 Telegram client(s) (personal_mcp, default)...
[08/12/26 00:36:16] INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connecting to 91.108.56.110:443/TcpFull...                                                   mtprotosender.py:234
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
                    INFO     Connection to 91.108.56.110:443/TcpFull complete!                                            mtprotosender.py:285
Warming entity caches (background)...
Telegram client(s) started (personal_mcp, default). Running MCP server (sse)...
INFO:     Started server process [91578]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8765 (Press CTRL+C to quit)
Entity caches warmed.
INFO:     127.0.0.1:54928 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54928 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54928 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54928 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54928 - "POST /sse HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:54928 - "GET /sse HTTP/1.1" 200 OK
INFO:     127.0.0.1:54929 - "POST /messages/?session_id=103e10fee8a64b578037f7d07507bbf9 HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:54929 - "POST /messages/?session_id=103e10fee8a64b578037f7d07507bbf9 HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:54929 - "POST /messages/?session_id=103e10fee8a64b578037f7d07507bbf9 HTTP/1.1" 202 Accepted
[08/12/26 00:36:43] INFO     Processing request of type ListToolsRequest                                                         server.py:674
INFO:     127.0.0.1:54996 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54996 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54996 - "POST /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54996 - "GET /mcp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54996 - "POST /sse HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:54996 - "GET /sse HTTP/1.1" 200 OK
INFO:     127.0.0.1:54997 - "POST /messages/?session_id=35cddac748c04cf6ae0793e176f2aa89 HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:54997 - "POST /messages/?session_id=35cddac748c04cf6ae0793e176f2aa89 HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:54997 - "POST /messages/?session_id=35cddac748c04cf6ae0793e176f2aa89 HTTP/1.1" 202 Accepted
[08/12/26 00:39:02] INFO     Processing request of type ListToolsRequest                                                         server.py:674
INFO:     127.0.0.1:54997 - "POST /messages/?session_id=35cddac748c04cf6ae0793e176f2aa89 HTTP/1.1" 202 Accepted
                    INFO     Processing request of type ListResourcesRequest                                                     server.py:674
INFO:     127.0.0.1:54997 - "POST /messages/?session_id=35cddac748c04cf6ae0793e176f2aa89 HTTP/1.1" 202 Accepted
                    INFO     Processing request of type ListPromptsRequest                                                       server.py:674
INFO:     127.0.0.1:55016 - "POST /messages/?session_id=35cddac748c04cf6ae0793e176f2aa89 HTTP/1.1" 202 Accepted
[08/12/26 00:40:03] INFO     Processing request of type CallToolRequest                                                          server.py:674
INFO:     127.0.0.1:55016 - "POST /messages/?session_id=35cddac748c04cf6ae0793e176f2aa89 HTTP/1.1" 202 Accepted

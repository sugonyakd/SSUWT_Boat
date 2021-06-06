from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
PHONE_NUMBER_GTF = env.str("PHONE_NUMBER_GTF")
EMAIL_GTF = env.str("EMAIL_GTF")
MAP = env.str("MAP")
VK_SHIP = env.str("VK_SHIP")
SITE_EMF = env.str("SITE_EMF")

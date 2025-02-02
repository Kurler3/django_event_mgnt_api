from dotenv import load_dotenv
import os
load_dotenv()

ENV_VAR_KEYS = {
    'SECRET_KEY': os.getenv('SECRET_KEY'),
    'JWT_SIGNING_KEY': os.getenv('JWT_SIGNING_KEY'),
}

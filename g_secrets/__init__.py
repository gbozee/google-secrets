import json
from .config_utils import Config
import click
import os


config = Config(os.path.abspath(".env"))


def build_client_secret(filename="client-secrets.json"):
    PROJECT_ID = config("G_PROJECT_ID")
    PRIVATE_KEY_ID = config("G_PRIVATE_KEY_ID")
    PRIVATE_KEY = config("G_PRIVATE_KEY")
    CLIENT_EMAIL = config("G_CLIENT_EMAIL")
    CLIENT_ID = config("G_CLIENT_ID")
    CLIENT_X509_CERT_URL = config("G_CLIENT_X509_CERT_URL")
    FILE_NAME = filename
    data = {
        "type": "service_account",
        "project_id": PROJECT_ID,
        "private_key_id": PRIVATE_KEY_ID,
        "private_key": PRIVATE_KEY,
        "client_email": CLIENT_EMAIL,
        "client_id": CLIENT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": CLIENT_X509_CERT_URL,
    }
    obj = ["{", ""]
    with open(filename, "w") as outfile:
        outfile.write("{")
        for i, (key, value) in enumerate(data.items()):
            string = f'"{key}": "{value}"'
            if i != len(data.items()) - 1:
                string += ","
            outfile.write(string)
        outfile.write("}")
        # json.dump(data, outfile, ensure_ascii=False)


@click.command()
@click.argument("file_name")
def create_secrets(file_name):
    """Generates google credentials.json from environmental variables."""
    build_client_secret(filename=file_name)
    click.echo("{} created".format(file_name))


if __name__ == "__main__":
    create_secrets()

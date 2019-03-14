## Google Secrets

A command line application that helps with the generation of Google API `credentials.json` files

### Usage

```bash
$ pip install -e <github_repo>

# create environmental variable consisting of the following
$ export G_PROJECT_ID=<>
$ export G_PRIVATE_KEY_ID=<>
$ export G_PRIVATE_KEY=<> 
$ export G_CLIENT_EMAIL=<>
$ export G_CLIENT_ID=<>
$ export G_CLIENT_X509_CERT_URL=<>

$ create-google-secrets credentials.json 
```
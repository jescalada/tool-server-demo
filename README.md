# Tool Server Demo

A simple Tool Server to demonstrate a JWT authorization flow in OpenWebUI.

### Environment Variables

These three environment variables are required for the server to run properly:

- `OIDC_CLIENT_ID`
- `OIDC_ISSUER`
- `JWKS_URL`

Here’s a sample .env configuration:

```env
OIDC_CLIENT_ID="<YOUR_CLIENT_ID>.apps.googleusercontent.com"
OIDC_ISSUER="https://accounts.google.com"
JWKS_URL="https://www.googleapis.com/oauth2/v3/certs"
```

You can export them manually or use a .env file with something like python-dotenv.

### Running the Server

First, create and activate a virtual environment (if desired):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Then install the requirements:

```bash
pip install -r requirements.txt
```

Start the server using uvicorn. I recommend running it on port 8081 to avoid conflicts with the OpenWebUI backend (which usually runs on 8080):

```bash
uvicorn mini_tool_server:app --reload --port 8081
```

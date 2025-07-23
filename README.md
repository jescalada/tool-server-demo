# Tool Server Demo

A simple Tool Server to demonstrate a JWT authorization flow in OpenWebUI.

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

### What this Tool Server does

This tool server demonstrates a JWT auth-protected Tool Server that echoes the latest message back to the user:

##### Sample interaction
![image](https://github.com/user-attachments/assets/5df57eb0-b1b5-44db-8e5a-fed3b674b6b5)

The actual response received by the LLM may differ depending on how OpenWebUI processed the Tool Server request. In this case, it ignored the `"Test Echo Server - "` and the `"echo_tool_tools_echo_post"` part. Note that OpenWebUI may not always make a request to the tool server (I believe this is because of limitations in the RAG implementation). In order to trigger the tool server request, try being as specific as possible in your prompt and try multiple times.

##### Tool Server Request and Response

![image](https://github.com/user-attachments/assets/5ee82095-ec1f-4b01-96e0-718b507b7aa7)

### Caveats/Troubleshooting

This tool server requires only an `access_token`. The `access_token` must be provided in the `Authorization` header in the form `Bearer <access-token>`. If you want to use this with OpenWebUI, you should `checkout` this specific PR: https://github.com/open-webui/open-webui/pull/14786
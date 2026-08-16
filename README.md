# Steps to use
1. Clone using `git clone https://github.com/vdroid1331/fastapi-blog.git`.
2. Change into the cloned repo using `cd fastapi-blog`.
3. Install the dependencies using `uv sync`.
4. Create a .env file by using the template given in .env.example.  
(Note: If you dont know how to create a secret key, you can run `python -c "import secrets; print(secrets.token_hex(32))"` on windows or `python3 -c "import secrets; print(secrets.token_hex(32))"` on Linux/Unix/MacOS.)
5. Run fastapi server in dev mode using `uv run fastapi dev`.

# Pre-Requisites
1. [Python 3.14+](https://www.python.org/downloads/).
2. [uv package manager](https://docs.astral.sh/uv/getting-started/installation/).
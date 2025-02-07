- Criar o virtual env
<p>python -m venv .venv</p>

- ativando o venv:
<p>source .venv/bin/activate (linux)</p>
<p>source .venv/Scripts/activate (windows bash)</p>
<p>.venv\Scripts\Activate.ps1 (windows powershell)</p>

- instalar dependências a partir do requirements.txt:
<p>pip install -r requirements.txt</p>

- atualização automática pós edição:
<p>uvicon main:app --reload</p>

- iniciar a aplicação
<p>fdastapi dev main.py</p>

- Sair do venv:
<p>deactivate</p>

- instalar as dependências do FastAPI:
dentro do venv:
<p>pip install "fastapi[standard]"</p>
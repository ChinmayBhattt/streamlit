1. uv installation
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


2. Initialized project `example` at `/home/user/example`
```bash
uv init my-app
```

3. Create a new script and add inline metadata declaring its dependencies:

```bash
uv add streamlit
```


4. Run the script in an isolated virtual environment:

```bash
uv streamlit run main.py
```

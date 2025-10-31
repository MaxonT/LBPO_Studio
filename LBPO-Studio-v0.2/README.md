# LBPO-Studio (Learning by Prompt Optimization) · v0.2

**What's new (v0.2):**
- 🌍 8-language UI (English, 简体中文, Español, Français, Deutsch, 日本語, 한국어, Português)
- 🌓 Theme: System / Light / Dark (auto remembers)
- ✨ Polished UI: icons, better cards, footer, hints
- 🍪 Cookie consent banner (preferences saved only after consent)
- 🔐 API key “remember locally” (opt‑in via localStorage)
- ⚖️ Legal pages: Terms, Privacy, Cookies
- 🧩 Same LBPO loop (mock & openai backends, evaluators, artifacts export)

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
cd /Users/yangming/Desktop/MVPs/LBPO_Studio/LBPO-Studio-v0.2
pip install -r requirements.txt
python3 app.py

# open http://localhost:5000
```

## Deploy (Render/Heroku/VM)
- Build: `pip install -r requirements.txt`
- Start: `python app.py`
- Env (optional): `OPENAI_API_KEY`, `PYTHON_VERSION=3.11`

License: MIT

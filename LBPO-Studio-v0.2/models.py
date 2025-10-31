import os, re
from typing import Optional
try:
    from openai import OpenAI
except Exception:
    OpenAI = None

class BaseModel:
    def complete(self, prompt: str, user_input: str) -> str:
        raise NotImplementedError

class MockModel(BaseModel):
    POS_WORDS = {"love","like","great","amazing","good","excellent","happy","enjoy"}
    NEG_WORDS = {"bad","terrible","awful","hate","angry","sad","worst","dislike"}

    def complete(self, prompt: str, user_input: str) -> str:
        txt = (user_input or "").lower()
        pos = sum(1 for w in self.POS_WORDS if w in txt)
        neg = sum(1 for w in self.NEG_WORDS if w in txt)
        if "sentiment" in prompt.lower() or "pos" in prompt.upper() or "NEG" in prompt.upper():
            return "POS" if pos >= neg else "NEG"
        return re.sub(r"\s+", " ", user_input or "").strip().upper()

class OpenAIModel(BaseModel):
    def __init__(self, model_name: str, api_key: Optional[str] = None):
        if OpenAI is None:
            raise RuntimeError("openai package not available. Install with `pip install openai`.")
        key = api_key or os.getenv("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("OPENAI_API_KEY is not set.")
        self.client = OpenAI(api_key=key)
        self.model = model_name or os.getenv("DEFAULT_MODEL", "gpt-4o-mini")

    def complete(self, prompt: str, user_input: str) -> str:
        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.0,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"[ERROR:{e}]"

def get_model(backend: str, model_name: str, api_key: Optional[str] = None) -> BaseModel:
    backend = (backend or "mock").lower()
    if backend == "openai":
        return OpenAIModel(model_name=model_name, api_key=api_key)
    return MockModel()

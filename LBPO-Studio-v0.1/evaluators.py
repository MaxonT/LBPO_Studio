import re
from typing import Callable

def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()

def exact_match(output: str, expected: str) -> float:
    return 1.0 if normalize(output) == normalize(expected) else 0.0

def keyword_f1(output: str, expected_keywords: str) -> float:
    out_tokens = set(t for t in re.findall(r"\w+", (output or "").lower()))
    kw = [k.strip().lower() for k in (expected_keywords or "").split(",") if k.strip()]
    if not kw:
        return 0.0
    hit = sum(1 for k in kw if k in out_tokens)
    precision = hit / max(1, len(out_tokens))
    recall = hit / max(1, len(kw))
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)

def get_evaluator(name: str) -> Callable[[str, str], float]:
    name = (name or "exact_match").lower()
    if name == "keyword_f1":
        return keyword_f1
    return exact_match

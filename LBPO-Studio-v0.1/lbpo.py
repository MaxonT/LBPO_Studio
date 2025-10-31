from typing import List, Dict, Any, Tuple
from models import get_model
from evaluators import get_evaluator

BASE_TEMPLATES = [
    "You are an expert system. Follow the task strictly.\nTask: {instruction}\nConstraints: Output only the final answer.",
    "You are a concise assistant.\nTask: {instruction}\nPlease return only the result, no extra text.",
    "Act as a careful solver.\nTask: {instruction}\nThink step by step, then output FINAL: <final>{{answer}}</final>.",
    "System: You are precise and deterministic.\nUser: {instruction}\nAssistant: Produce the answer only.",
    "Role: Domain specialist.\nGoal: {instruction}\nRules: Be unambiguous, deterministic, and format exactly as requested.",
]

MUTATIONS = [
    "Add rule: Do not include apologies or hedging language.",
    "Add rule: Avoid explanations; answer only with the required token(s).",
    "Add rule: If uncertain, choose the most likely label deterministically.",
    "Add rule: Normalize case to uppercase.",
    "Add rule: Wrap the final answer in <final> tags.",
]

def generate_candidates(instruction: str, beam_width: int) -> List[str]:
    seeds = [tpl.format(instruction=instruction) for tpl in BASE_TEMPLATES]
    expanded = []
    for s in seeds:
        expanded.append(s)
        for m in MUTATIONS:
            expanded.append(s + "\n" + m)
    return expanded[: max(beam_width * 3, beam_width)]

def run_optimization(
    instruction: str,
    testcases: List[Dict[str, str]],
    backend: str,
    evaluator: str,
    model_name: str,
    api_key: str,
    iterations: int = 3,
    beam_width: int = 5,
) -> Dict[str, Any]:
    model = get_model(backend, model_name=model_name, api_key=api_key)
    eval_fn = get_evaluator(evaluator)

    candidates = generate_candidates(instruction, beam_width)
    leaderboard: List[Tuple[float, str]] = []

    for _ in range(iterations):
        scored = []
        for prompt in candidates:
            total = 0.0
            for case in testcases:
                _in = case.get("input", "")
                _exp = case.get("expected", "")
                out = model.complete(prompt, _in)
                total += eval_fn(out, _exp)
            avg_score = total / max(1, len(testcases))
            scored.append((avg_score, prompt))
        scored.sort(key=lambda x: x[0], reverse=True)
        topk = scored[:beam_width]
        leaderboard.extend(topk)
        next_candidates = []
        for score, p in topk:
            for m in MUTATIONS:
                next_candidates.append(p + "\n" + m)
        candidates = list({c for c in next_candidates})[: max(beam_width * 3, beam_width)]

    seen = set()
    uniq = []
    for s, p in leaderboard:
        if p not in seen:
            uniq.append({"score": round(s, 4), "prompt": p})
            seen.add(p)
    uniq.sort(key=lambda x: x["score"], reverse=True)
    best = uniq[0] if uniq else {"score": 0.0, "prompt": instruction}

    return {
        "instruction": instruction,
        "backend": backend,
        "evaluator": evaluator,
        "leaderboard": uniq[:50],
        "best": best,
    }

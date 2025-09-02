import re
from aries.config import SYSTEM_PROMPT, MAX_PROMPT_CHARS

CANNED_PATTERNS = [
    r"if you have any (questions|other).*",
    r"feel free to ask.*",
    r"how can i (help|assist) you.*",
    r"let me know if you need.*",
    r"if you want, i can.*"
]
CANNED_RE = re.compile(r"(?:\n|\r|\s)*(" + r"|".join(CANNED_PATTERNS) + r")(?:\n|\.|!|\?)?", flags=re.IGNORECASE)

def clean_ai_text(text):
    cleaned = CANNED_RE.sub("", text).strip()
    if cleaned and cleaned[-1] not in ".!?":
        cleaned += "."
    return cleaned

def build_prompt_with_memory(user_input, memory):
    prompt_parts = [SYSTEM_PROMPT]
    rev = list(reversed(memory))
    mem_lines = []
    total_len = len(SYSTEM_PROMPT)
    for entry in rev:
        snippet = f"User: {entry.get('input','')}\nAI: {entry.get('output','')}\n"
        if total_len + len(snippet) + len(user_input) > MAX_PROMPT_CHARS:
            break
        mem_lines.insert(0, snippet)
        total_len += len(snippet)
    if mem_lines:
        prompt_parts.append("Conversation history:\n")
        prompt_parts.extend(mem_lines)
    prompt_parts.append(f"User: {user_input}\nAI:")
    return "\n".join(prompt_parts)



def input_guardrails_node(state):
    input_text = state.get("input", "").lower()

    blocked_words = [
        "bomb", "weapon", "sex", "nude", "drug", "hack", "explosive"
    ]

    for word in blocked_words:
        if word in input_text:
            return {
                "blocked": True,
                "reason": "Identified malicious intent"
            }

    return {"blocked": False}



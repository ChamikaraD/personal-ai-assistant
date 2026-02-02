

def input_guardrails_node(state):
    input_text = state.get("input", "").lower()

    blocked_words = [
        "bomb", "weapon", "sex", "nude", "drug", "hack", "explosive",
        "bomb", "explosive", "grenade", "gun", "rifle", "pistol",
        "weapon", "knife", "shoot", "shooting", "assault",
        "terrorist", "terrorism", "isis", "al-qaeda",
        "attack", "massacre", "kill", "murder", "assassinate",
        "drug", "cocaine", "heroin", "meth", "methamphetamine",
        "lsd", "ecstasy", "mdma", "weed", "marijuana", "cannabis",
        "opioid", "fentanyl", "overdose", "dealer", "smuggle",
        "hack", "hacking", "cracker", "phishing", "malware",
        "ransomware", "spyware", "keylogger",
        "ddos", "botnet", "bruteforce",
        "steal password", "credential", "breach",
        "sex", "sexual", "nude", "nudity", "porn", "pornography",
        "explicit", "xxx", "fetish", "erotic",
        "escort", "prostitute", "onlyfans",
        "child porn", "cp", "underage sex",
        "minor nude", "sexualize children"
    ]

    for word in blocked_words:
        if word in input_text:
            return {
                "blocked": True,
                "reason": "Identified malicious intent"
            }

    return {"blocked": False}



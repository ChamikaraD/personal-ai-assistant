from graph import compiled_graph


def execute_graph(user_input: str):
    result = compiled_graph.invoke({"input": user_input})

    # Handle blocked input
    if result.get("blocked"):
        return f"🚫 Blocked\n\nReason: {result.get('reason')}"

    agent = result.get("agent", "unknown")
    response = result.get("response", "")

    # Ensure clean text (no AIMessage object)
    if hasattr(response, "content"):
        response_text = response.content
    else:
        response_text = str(response)

    return f"Agent Used: {agent.upper()}\n\n{response_text}"


if __name__ == "__main__":
    while True:
        user_input = input("Ask a question: ")
        print(execute_graph(user_input))

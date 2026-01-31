from graph import compiled_graph


def execute_graph(user_input: str):
    result = compiled_graph.invoke({"input": user_input})

    if result.get("blocked"):
        return result.get("reason")

    response = result.get("response")


    if hasattr(response, "content"):
        return response.content

    return str(response)


if __name__ == "__main__":
    while True:
        user_input = input("Ask a question: ")
        print(execute_graph(user_input))
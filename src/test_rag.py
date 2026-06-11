from rag import ask_question

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        break

    answer = ask_question(question)

    print("\nAnswer:")
    print(answer)
    print()
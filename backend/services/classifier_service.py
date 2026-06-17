from services.llm_service import generate_response

def classify_email_service(email: str):

    with open("prompts/classify_prompt.txt", "r", encoding="utf-8") as file:
        prompt_template = file.read()

    prompt = prompt_template.format(email=email)

    category = generate_response(prompt)

    return {
        "received_email": email,
        "category": category.strip()
    }
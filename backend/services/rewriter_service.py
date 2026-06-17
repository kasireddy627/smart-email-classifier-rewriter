from services.llm_service import generate_response

def rewrite_email_service(email: str, tone: str):

    with open("prompts/rewrite_prompt.txt", "r", encoding="utf-8") as file:
        prompt_template = file.read()

    prompt = prompt_template.format(
        email=email,
        tone=tone
    )

    rewritten_email = generate_response(prompt)

    return {
    "rewritten_email": rewritten_email.strip()
    }
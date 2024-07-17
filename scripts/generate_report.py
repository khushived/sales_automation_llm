import gemini

gemini.api_key = "AIzaSyAYjwOuigc03kLqMBlKwQeyrlW9PmW4n60"

def generate_report_with_llm(data):
    """Generates a report using an LLM to create human-readable content."""
    prompt = f"Generate a comprehensive sales report based on the following data: {data}"
    response = gemini.ChatCompletion.create(
        model="gemini-llm",  # Choose an appropriate Gemini LLM model
        messages=[
            {"role": "system", "content": "You are an expert report writer."},
            {"role": "user", "content": prompt}
        ]
    )
    report_content = response.choices[0].text
    return report_content

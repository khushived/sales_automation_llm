from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

def generate_report_with_llm(data):
    """Generates a report using an LLM to create human-readable content."""
    prompt = f"Generate a comprehensive sales report based on the following data: {data}"

    # Initialize the transformer pipeline for text generation
    model_name = "distilgpt2"  # Example model, you can choose based on your needs
    generator = pipeline("text-generation", model=model_name)

    # Generate report content based on the prompt
    report_content = generator(prompt, max_length=250, num_return_sequences=1)[0]['generated_text']
    
    return report_content

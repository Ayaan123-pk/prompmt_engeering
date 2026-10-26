from groq import generate_response
def prompt_engineering_activity():
    print("Welcome to the Prompt Engineering Activity!")
    vague = input("Please enter a vague prompt: ")
    print("\nAI's response to your vague prompt:")
    print(generate_response(vague))
    specific = input("\nNow, please enter a more specific prompt: ")
    print("\nAI's response to your specific prompt:")
    print(generate_response(specific))
    context = input("\nFinally, please enter a prompt with context: ")
    print("\nAI's response to your contextual prompt:")
    print(generate_response(context))
    print("\n--- Reflection---")
    print("1. How did the AI's responses differ based on the specificity of your prompts?")
    print("2. What strategies can you use to improve your prompts for better AI responses?")
    print("3. How can you apply these prompt engineering techniques in real-world scenarios?")

if __name__ == "__main__":
    prompt_engineering_activity()

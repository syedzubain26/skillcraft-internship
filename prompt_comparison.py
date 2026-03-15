# SkillCraft Internship
# Task 01 - Writing Better Prompts

vague_prompts = [
    "Explain climate change",
    "Tell me about AI",
    "Give startup ideas"
]

improved_prompts = [
    "Explain climate change in 3 bullet points for a 12-year-old student",
    "Explain Artificial Intelligence with 3 real-life examples in simple language",
    "Suggest 3 AI startup ideas for students with limited budget"
]

vague_outputs = [
    "Climate change refers to long term shifts in temperature and weather patterns.",
    "AI is the simulation of human intelligence by machines.",
    "You can start technology companies using AI."
]

improved_outputs = [
    "• Earth is getting warmer due to pollution\n• Ice caps are melting\n• This affects animals and weather",
    
    "• Voice assistants like Alexa\n• Netflix recommendation system\n• Self-driving cars",
    
    "• AI Resume Builder for students\n• AI Study Planner\n• AI Budget Tracker App"
]

print("\nPROMPT COMPARISON RESULTS\n")

for i in range(3):
    
    print("Vague Prompt:", vague_prompts[i])
    print("Output:", vague_outputs[i])
    
    print("\nImproved Prompt:", improved_prompts[i])
    print("Output:", improved_outputs[i])
    
    print("\n-----------------------------\n")
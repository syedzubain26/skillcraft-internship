# Prompt Engineering Creativity Test
# SkillCraft Internship Task 02

prompts = [
    "Generate 3 creative startup ideas using AI technology.",
    "You are a startup mentor. Suggest 3 innovative AI startup ideas that solve real world problems.",
    "Act like Elon Musk. Suggest futuristic AI startup ideas for the next 10 years."
]

responses = [
    [
        "AI Fitness Coach App",
        "AI Personal Finance Advisor",
        "AI Travel Planner"
    ],
    [
        "AI Crop Disease Detection for Farmers",
        "AI Mental Health Chat Support",
        "AI Resume Builder for Students"
    ],
    [
        "AI Colony Builder for Mars",
        "Neural AI Brain Interface Startup",
        "Autonomous AI City Management System"
    ]
]

print("\nPROMPT ENGINEERING RESULTS\n")

for i in range(len(prompts)):
    print("Prompt:", prompts[i])
    print("Generated Ideas:")
    
    for idea in responses[i]:
        print("-", idea)
    
    print("\n---------------------------\n")
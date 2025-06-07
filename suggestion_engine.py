def generate_suggestion(feedback):
    feedback = feedback.lower()
    
    if "spicy" in feedback:
        return "Consider reducing spice levels or offering curd."
    elif "oil" in feedback or "oily" in feedback:
        return "Try using less oil or switching to steamed options."
    elif "cold" in feedback:
        return "Ensure food is kept warm before serving."
    elif "undercooked" in feedback:
        return "Double-check cooking time for rice or vegetables."
    elif "sour" in feedback:
        return "Check ingredients freshness and cooking time."
    else:
        return "Thank you for your feedback! We'll work on improving."

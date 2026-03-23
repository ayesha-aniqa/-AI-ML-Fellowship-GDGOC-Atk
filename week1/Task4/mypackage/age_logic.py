def age_check(age):
    try:
        age_int = int(age)
        if age_int >= 18:
            return "Access Granted"
        else:
            return f"Access Denied: You are underage."
    except ValueError:
        return "Error: Please enter a valid number for age."
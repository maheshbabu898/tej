def login(username, password):
    # Simple hardcoded login logic
    if username == "admin" and password == "password123":
        return "Login successful"
    else:
        return "Invalid credentials"

def cors_is_valid(request, methods_allowed):
    headers = request.headers
    if request.method == "OPTIONS":
        return True
    return False
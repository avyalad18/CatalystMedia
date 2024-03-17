

def getSerializerErrorDetails(e):
    error_messages = []
    for field_errors in e.detail.values():
        if isinstance(field_errors, list):
            for error in field_errors:
                error_messages.append(str(error))
        else:
            error_messages.append(str(field_errors))
    
    # Join the error messages into a single string
    error_message = "  ".join(error_messages)
    return error_message
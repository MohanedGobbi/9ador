def extract_search_query(input_string,string_to_extract):
    # Define the phrase you want to remove from the input
    prefix = string_to_extract

    # Check if the input string starts with the desired prefix
    if input_string.lower().startswith(prefix):
        # Remove the prefix and strip any leading or trailing spaces
        query = input_string[len(prefix):].strip()
        return query
    else:
        return None

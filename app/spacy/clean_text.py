import re


def text_cleaner(text):
    # Remove all emojis which don't contribute anything.
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    text = re.sub(emoji_pattern, ' ', text)

    # List of cleaning rules to apply on the text
    rules = [
        {r'>\s+': u'>'},  # remove spaces after a tag opens or closes
        {r'\s+': u' '},  # replace consecutive spaces with a single space
        {r'\s*<br\s*/?>\s*': u'\n'},  # replace <br> tags with a newline
        # add a newline after closing div, p, or h1-h6 tags
        {r'</(div)\s*>\s*': u'\n'},
        {r'</(p|h\d)\s*>\s*': u'\n\n'},
        {r'<head>.*<\s*(/head|body)[^>]*>': u''},  # remove the entire <head> section
        {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  # replace <a> tags with their href attribute content
        {r'[ \t]*<[^<]*?/?>': u''},  # remove any remaining tags
        {r'^\s+': u''}  # remove spaces at the beginning of the text
    ]

    # Apply each rule sequentially to the text
    for rule in rules:
        for (pattern, replacement) in rule.items():
            regex = re.compile(pattern)
            text = regex.sub(replacement, text)
    
    # Remove trailing spaces
    text = text.rstrip()
    return text


def text_formatter(text):
    if text is None:
        return ""

    # Apply substitutions to improve text format
    text = re.sub(r':\s*', ' ', text)  # replace colon followed by spaces with a single space
    text = re.sub(r'&', ', ', text)  # replace ampersands with commas and a space
    text = re.sub(r'/', ', ', text)  # replace slashes with commas and a space
    text = re.sub(r'\.*\n\.*', '.', text)  # replace newlines surrounded by dots with a period
    text = re.sub(r'^[dD][rR](\.|\s*)*', 'Dr. ', text)  # standardize 'Dr.' at the beginning of the text
    text = re.sub(r'\s[dD][rR](\.|\s*)*', ' Dr. ', text)  # standardize 'Dr.' in the middle of the text
    
    return text

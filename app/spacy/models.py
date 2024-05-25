import spacy

# Define the name of the spaCy model to use
MODEL_NAME = 'en_core_web_md'

def get_model():
    # Check if the specified model is already installed
    if not spacy.util.is_package(MODEL_NAME):
        # If the model is not installed, download it using spaCy's command-line interface
        spacy.cli.download(MODEL_NAME)
        print(f"\033[92mSpacy model has downloaded!")
    
    # Load the specified spaCy model
    ner_model = spacy.load(MODEL_NAME)
    
    # Print a confirmation message that the model has been successfully loaded
    print(f"Spacy model named {ner_model.meta.get('name')} has loaded!\033[0m")
    
    # Return the loaded model for further use
    return ner_model

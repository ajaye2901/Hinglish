from translate import Translator

def hinglish_translation(text):
    translator = Translator(to_lang="hi")

    # Define a list of words to keep in English
    # english_words = ["feedback", "video", "products", "waiting"]

    # Split the input text into sentences
    sentences = text.split('.')

    hinglish_sentences = []
    for sentence in sentences:
        # Split the sentence into words
        words = sentence.split()

        # Initialize an empty list to store translated words
        translated_words = []

        for word in words:
            # Translate the word to Hindi
            translation = translator.translate(word)

            # Replace certain English words with their Hinglish equivalents
            hinglish_word = {
                "feedback": "feedback",
                "video": "video",
                "products": "products",
                "waiting": "waiting"
            }.get(word.lower(), translation)

            translated_words.append(hinglish_word)

        # Join the words back into a sentence
        hinglish_sentence = ' '.join(translated_words)
        hinglish_sentences.append(hinglish_sentence)

    # Join the sentences back into a paragraph
    hinglish_text = '. '.join(hinglish_sentences)

    return hinglish_text

# Example usage:
english_text ="So even if it's a big video, I will clearly mention all the products"
hinglish_text = hinglish_translation(english_text)
print(hinglish_text)

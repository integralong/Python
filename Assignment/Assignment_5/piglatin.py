#Lauren Song
#U79789182
#Pig Latin Translator


def rule_convert_to_pig_latin(word):
    if len(word) == 1:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

def translate_text_to_pig_latin(input_text):
    words = input_text.split()
    pig_latin_text = ''

    for word in words:
        pig_latin_text += rule_convert_to_pig_latin(word) + ' '

    if pig_latin_text:
        pig_latin_text = pig_latin_text[:-1]
    return pig_latin_text
        

def main():
    input_file_name = input("Enter the name of a text file (in .txt format):")

    with open(input_file_name, 'r') as input_file:
        text = input_file.read()
        text = text.lower()  # Convert text to lowercase
        pig_latin_text = translate_text_to_pig_latin(text)
        
    output_file_name = input("Enter the name of the translated text file:")

    with open(output_file_name, 'w') as output_file:
        output_file.write(pig_latin_text)
        print(f'{output_file_name} translated to Pig Latin and saved.')

if __name__ == "__main__":
    main()

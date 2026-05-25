
# str.maketrans(): method takes two equal length os string and returns a translation table that maps each chracter of the first string with the corrosponding character of the second string; each character of the translation table stroed as unique number as number list;


# Translate()  method takes as argument translation table and it is called on string and return the copy  of the string where each character is replaced based on the translation table;

def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return "Shift must be an integer value"
    
    if shift < 1 or shift > 25:
        return "shift must an integer between 1 and 25"
    
    if encrypt == 0:
        shift = -shift
   
    alphabet = 'abcdefghijklmnopqrstuvwxyz';
    shifted_alphabet = alphabet[shift:] + alphabet[:shift];
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper());
    return text.translate(translation_table);


def encrypt(text, shift):
    return caesar(text, shift);
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False);

encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf.";
decrypted_text = decrypt(encrypted_text, 13);
print(decrypted_text);
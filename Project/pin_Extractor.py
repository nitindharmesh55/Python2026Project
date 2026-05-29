def pin_extractor(poems):
    secret_codes = []

    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')

        for line_index, line in enumerate(lines):
            words = line.split()

            if line_index < len(words):
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"

        secret_codes.append(secret_code)

    return secret_codes
     
  











poem = """The morning sun begins to rise,
Painting gold across the skies.
Birds awaken, singing clear,
Welcoming a day sincere.
Gentle winds through branches play,
Carrying dreams into the day."""

print(pin_extractor([poem]))
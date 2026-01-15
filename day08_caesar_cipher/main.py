import art

print(art.logo)

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabets:
            shift_position = alphabets.index(letter) + shift_amount
            output_text += alphabets[shift_position % 26]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d text: {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid choice.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift:\n")) % 26

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")

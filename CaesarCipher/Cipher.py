from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, direction):
   final_text=""
   for ch in text:
      if ch in alphabet:
        i=alphabet.index(ch)
        #encrypt
        if(direction=="encode"):
         if(i+shift<len(alphabet)):
           final_text+=alphabet[i+shift]
         else:
           final_text+=alphabet[i+shift-len(alphabet)]
        #decrypt
        else:
         final_text+=alphabet[i-shift]
      else:
        final_text+=ch
   print(f"The {direction}d is {final_text}.")

result="yes"
while(result=="yes"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = (int(input("Type the shift number:\n")))%26
  caesar_cipher(text, shift, direction)
  result=(input("Type 'yes' if you want to go again. Otherwise type 'no'.")).lower()

print("Goodbye!")
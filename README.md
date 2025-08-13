How it works:

The caesar_cipher_encrypt function takes your message and, for every letter, moves it forward in the alphabet by the "shift" number you provide. For instance, if you enter a shift of 3, then 'A' becomes 'D', 'B' becomes 'E', and so on. If the letter goes past 'Z', it wraps around to the start of the alphabet again. Importantly, any characters that aren't letters—like spaces, numbers, or punctuation—stay exactly as they are.

The caesar_cipher_decrypt function reverses the process. Instead of moving letters forward, it moves them backward by the same shift amount. This way, your original message is restored as long as you use the same shift value.

In summary, letters are shifted according to your input, while everything else in the text is left unchanged. This makes the Caesar cipher simple but effective for basic secret messages!

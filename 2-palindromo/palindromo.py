def eh_palindromo(texto):
    return texto.replace(" ", "").lower() == texto.replace(" ", "").lower()[::-1]

print(eh_palindromo("Ame a ema"))  
print(eh_palindromo("Olá"))        

def x_language_keyword_automaton(input_string):
    keywords = set(["int", "float", "while", "main", "const"])
    token = ""
    i = 0

    while i < len(input_string):
        char = input_string[i]

        if char.isalpha():
            token += char
        else:
            if token in keywords:
                yield (token, token)
            token = ""

        i += 1

    if token in keywords:
        yield (token, token)

input_string = "int main(){const float payment = 384.00; float bal; int month = 0; bal=15000; while (bal>0){printf('Month: %2d Balance: %10.2f\\n', month, bal); bal=bal-payment+0.015*bal; month=month+1;}"
for token, lexeme in x_language_keyword_automaton(input_string):
    print(f"Token: {token}, Lexeme: {lexeme}")

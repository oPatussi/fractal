import turtle

def apply_rule(symbol, rules):
    """
    Aplica a regra de produção correspondente ao símbolo fornecido.
    Retorna a sequência de símbolos resultante da aplicação da regra.
    """
    return rules.get(symbol, symbol)

def generate_string(axiom, rules, iterations):
    """
    Gera a sequência de símbolos correspondente à curva de Hilbert
    a partir do axioma fornecido e das regras de produção.
    """
    string = axiom
    for i in range(iterations):
        new_string = ""
        for symbol in string:
            new_string += apply_rule(symbol, rules)
        string = new_string
    return string

def draw_hilbert_curve(turtle, string, size):
    """
    Desenha a curva de Hilbert utilizando a sequência de símbolos fornecida.
    """
    for symbol in string:
        if symbol == "F":
            turtle.forward(size)
        elif symbol == "-":
            turtle.left(90)
        elif symbol == "+":
            turtle.right(90)

# Define o axioma e as regras de produção
axiom = "X"
rules = {"X": "-YF+XFX+FY-",
         "Y": "+XF-YFY-FX+"}

# Gera a sequência de símbolos correspondente à curva de Hilbert
string = generate_string(axiom, rules, 8)

# Configurações iniciais da turtle
turtle.speed(0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

# Desenha a curva de Hilbert
draw_hilbert_curve(turtle, string, 10)

# Mantém a janela aberta até o usuário fechar
turtle.done()

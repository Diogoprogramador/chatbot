import random
import datetime

# Respostas predefinidas para várias categorias
respostas = {
    "oi": ["Olá! Como posso te ajudar?", "Oi! Tudo bem?", "Olá, como você está?"],
    "como vai?": ["Estou bem, e você?", "Estou ótimo, obrigado por perguntar!", "Vou indo, e você?"],
    "qual seu nome?": ["Eu sou uma IA sem nome! Você pode me chamar de como quiser.", "Me chame como preferir.",
                       "Eu sou o Chatbot, mas me diga como você gostaria que eu fosse chamada."],
    "tchau": ["Até logo!", "Tchau, tenha um ótimo dia!", "Até a próxima!"],

    # Curiosidades sobre o Brasil
    "qual a capital do brasil?": ["A capital do Brasil é Brasília.",
                                  "A capital do Brasil é Brasília, uma cidade planejada."],
    "qual é a comida típica do brasil?": ["Feijoada é uma das comidas mais típicas do Brasil.",
                                          "A comida típica do Brasil varia muito, mas a feijoada é bem conhecida."],
    "qual é o time mais popular do brasil?": ["O Flamengo é o time mais popular do Brasil.",
                                              "O Flamengo, com sua enorme torcida, é o time mais popular no Brasil."],

    # Perguntas sobre clima e tempo
    "qual o clima hoje?": ["Desculpe, eu não posso acessar a previsão do tempo no momento.",
                           "Não tenho informações sobre o clima, mas você pode conferir em um site de previsão."],

    # Perguntas sobre saúde
    "como posso melhorar minha saúde?": [
        "A prática regular de exercícios e uma alimentação equilibrada são fundamentais para a saúde.",
        "Tente incluir mais frutas e vegetais na sua dieta e beber muita água!"],
    "o que é uma alimentação saudável?": [
        "Uma alimentação saudável inclui uma variedade de alimentos, como frutas, vegetais, proteínas magras e grãos integrais.",
        "É importante evitar alimentos processados e excessivamente açucarados para manter uma boa saúde."],

    # Perguntas sobre matemática básica
    "quanto é 2 + 2?": ["2 + 2 é igual a 4.", "O resultado de 2 + 2 é 4."],
    "quanto é 10 * 10?": ["10 vezes 10 é igual a 100.", "O resultado de 10 * 10 é 100."],

    # Perguntas sobre data e hora
    "qual é a data de hoje?": [f"A data de hoje é {datetime.datetime.now().strftime('%d/%m/%Y')}.",
                               "Hoje é " + datetime.datetime.now().strftime("%A, %d de %B de %Y.")],
    "que horas são?": [f"As horas são {datetime.datetime.now().strftime('%H:%M:%S')}.",
                       f"Agora são {datetime.datetime.now().strftime('%H:%M:%S')}."],

    # Perguntas genéricas e respostas
    "me conte uma piada": ["Por que o livro de matemática se suicidou? Porque tinha muitos problemas!",
                           "O que é um vegetariano que come carne? Um ex-vegetariano!"],
    "quem é você?": ["Eu sou uma IA criada para ajudar e conversar com você. Como posso te ajudar hoje?",
                     "Eu sou um assistente virtual. Pergunte o que quiser!"]
}


def responder(pergunta):
    pergunta = pergunta.lower().strip()

    # Se a pergunta for uma das chaves no dicionário, retorna uma resposta aleatória
    if pergunta in respostas:
        return random.choice(respostas[pergunta])

    # Caso não haja resposta predefinida, retorna uma resposta padrão
    return "Desculpe, não entendi. Pode reformular?"


def interagir(nome_ia):
    print(f"Olá! Eu sou {nome_ia}. Como posso te ajudar?")

    while True:
        pergunta = input(f"{nome_ia}: ")

        # Se o usuário disser 'tchau', a conversa termina
        if pergunta.lower() == "tchau":
            print(f"{nome_ia}: Até logo!")
            break

        resposta = responder(pergunta)
        print(f"{nome_ia}: {resposta}")


def obter_nome():
    nome = input("Escolha um nome para sua IA: ")
    return nome.strip()


# Inicia o programa
nome_ia = obter_nome()
interagir(nome_ia)

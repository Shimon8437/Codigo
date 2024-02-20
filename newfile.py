from unidecode import unidecode

pares = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como te llamas": "Soy un chatbot. Puedes llamarme ChatGPT",
    "que hora es": "No tengo la capacidad de decir la hora",
    "adios": "¡Hasta luego! Adiós",
    "como estas": ["Estoy bien, gracias por preguntar.", "Podría estar mejor."],
    "cual es tu funcion": "Soy un asistente virtual diseñado para ayudarte con información y preguntas.",
    "quien te creo": "Fui desarrollado por Shimon Feldman de OpenAI.",
    "capital de chile": "La capital de Chile es Santiago.",
    "capital de peru": "La capital de Perú es Lima.",
    "capital de argentina": "La capital de Argentina es Buenos Aires.",
    "capital de brasil": "La capital de Brasil es Brasilia.",
    "triple alianza": "La Triple Alianza fue una coalición formada por Alemania, Austria-Hungría e Italia durante la Primera Guerra Mundial.",
    "quien gano la segunda guerra mundial": "Los Aliados, liderados por Estados Unidos, la Unión Soviética y el Reino Unido, ganaron la Segunda Guerra Mundial.",
    "mundial de 2022": "La Copa Mundial de la FIFA 2022 se llevó a cabo en Qatar. Para obtener información detallada sobre los resultados, te recomiendo buscar en fuentes actualizadas.",
    "torres gemelas": "El 11 de septiembre de 2001, las Torres Gemelas en Nueva York fueron atacadas por terroristas. Este evento llevó a Estados Unidos a tomar medidas significativas en la lucha contra el terrorismo.",
    "san martin": "José de San Martín lideró la lucha por la independencia en América del Sur. Liberó a Chile en 1818 y a Perú en 1821, contribuyendo a la independencia de estas naciones.",
    "revolucion industrial": "La Revolución Industrial fue un período de transformación económica y social que comenzó en el siglo XVIII en Inglaterra. Marcó el cambio de la producción artesanal a la industrialización.",
    "caída del muro de berlín": "El 9 de noviembre de 1989, el Muro de Berlín, que dividía Alemania durante la Guerra Fría, cayó, simbolizando el fin de la división entre el este y el oeste.",
    "revolución rusa": "En 1917, la Revolución Rusa condujo al derrocamiento del gobierno zarista y al establecimiento del régimen comunista bajo el liderazgo de Vladimir Lenin.",
    "tratado de versalles": "El Tratado de Versalles, firmado en 1919 al final de la Primera Guerra Mundial, impuso condiciones y sanciones a Alemania, contribuyendo a tensiones geopolíticas que llevaron a la Segunda Guerra Mundial.",
    "apartheid en sudáfrica": "El apartheid en Sudáfrica fue un sistema de segregación racial institucionalizado que existió desde 1948 hasta principios de la década de 1990, antes de la transición a un gobierno democrático.",
    "llegada a la luna": "El 20 de julio de 1969, la misión Apolo 11 de la NASA logró el primer alunizaje tripulado con Neil Armstrong y Buzz Aldrin, marcando un hito en la exploración espacial.",
    "copa del mundo": "La Copa Mundial de la FIFA es el torneo internacional de fútbol más importante. Se celebra cada cuatro años, y equipos de todo el mundo compiten por el título.",
    "liga de campeones": "La Liga de Campeones de la UEFA es el torneo de clubes de fútbol más prestigioso de Europa, donde los mejores equipos compiten por el título.",
    "copa américa": "La Copa América es el torneo de fútbol más antiguo del mundo a nivel de selecciones nacionales de América del Sur, y ha sido escenario de emocionantes encuentros a lo largo de los años.",
    "balón de oro": "El Balón de Oro es un prestigioso premio individual otorgado al mejor jugador de fútbol del mundo cada año. Ha sido una distinción codiciada desde su creación en 1956.",
    "revolucion francesa": "La Revolución Francesa fue un periodo de cambio político y social que tuvo lugar en Francia entre 1789 y 1799, marcado por la abolición de la monarquía y el ascenso de la República.",
    "independencia de estados unidos": "La Independencia de Estados Unidos se declaró el 4 de julio de 1776, marcando el surgimiento de los Estados Unidos como una nación soberana, separada del dominio británico.",
    "caída del imperio romano": "La caída del Imperio Romano ocurrió en el año 476 d.C., marcando el fin de la antigua Roma y el comienzo de la Edad Media en Europa.",
    "revolución china": "La Revolución China, liderada por el Partido Comunista y Mao Zedong, culminó en 1949 con la fundación de la República Popular China, marcando un cambio significativo en la historia del país."
}

def limpiar_texto(texto):
    texto_sin_acentos = unidecode(texto)
    return ''.join(caracter for caracter in texto_sin_acentos if caracter.isalnum() or caracter.isspace()).lower()

def chatbot_responder(mensaje_usuario):
    mensaje_usuario_limpio = limpiar_texto(mensaje_usuario)
    respuesta = next((respuesta for patron, respuesta in pares.items() if limpiar_texto(patron) in mensaje_usuario_limpio), None)
    return respuesta if respuesta else "Lo siento, no entiendo la pregunta o no tengo información sobre eso."

print("¡Hola! Soy un chatbot desarrollado por Shimon Feldman de OpenAI. Puedes comenzar a preguntarme.")
while True:
    mensaje_usuario = input("Tú: ")
    if mensaje_usuario.lower() == 'salir':
        break
    respuesta = chatbot_responder(mensaje_usuario)
    print("Chatbot:", respuesta)
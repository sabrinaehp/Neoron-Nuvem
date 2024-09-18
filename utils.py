import json
import webbrowser
import xml.etree.ElementTree as ET
from datetime import datetime


def verificar_diferenca_hora(hora1: str, hora2: str) -> bool:
    try:
        # Converte os horários para objetos datetime
        tempo1 = datetime.strptime(hora1, "%H:%M")
        tempo2 = datetime.strptime(hora2, "%H:%M")

        # Calcula a diferença absoluta entre os horários
        diferenca = abs((tempo2 - tempo1).total_seconds())

        # Checa se a diferença é de 1800 segundos (30 minutos) ou menos
        print("000")
        return diferenca <= 1800

    except ValueError:
        return False


def validar_hora(hora: str) -> bool:
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False


def validar_data(data: str) -> bool:
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def linkedin_link() -> None:
    url = "https://www.linkedin.com/in/sabrina-holanda-7143611a5"
    webbrowser.open(url)


if __name__ == "__main__":
    print(verificar_diferenca_hora("18:20", "19:40"))

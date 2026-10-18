from colorama import Fore, Style, init

#Inicializa o colorama para garantir o funcionamento correto das cores no terminal
init(autoreset=True)

# Lista que armazena os dados dos níveis 
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
  ]

# Função que vai definir e exibir a mensagem do nível informado
def monitorar_reservatorio(nivel_informado):
  # Procura o nível correspondente na lista
  for item in niveis_reservatorio:
    if item["nivel"] == nivel_informado:
      # Exibe a situação com a cor correspondente
      print(
          f"{item['cor']}[Nível {item['nivel']}] Situação do reservatório:"
          f" {item['situacao']}{Style.RESET_ALL}"
      )
      return

  print(f"{Fore.RED}Erro: Nível inválido informado!{Style.RESET_ALL}")

# Simulação do monitoramento com valores definidos no código
if __name__ == "__main__":
  print("=== Sistema de Monitoramento de Reservatório de Água ===")
  print("Simulando leituras consecutivas do sensor:\n")

  # Simulando diferentes leituras do reservatório
  leituras_simuladas = [1, 3, 5, 2, 4]

  for leitura in leituras_simuladas:
    monitorar_reservatorio(leitura)

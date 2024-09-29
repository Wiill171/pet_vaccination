# Definindo a classe Pet
class Pet:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.vacinas = []
        self.historico_doencas = []
        self.medicamentos = []

    def adicionar_vacina(self, vacina, data, veterinario, crv):
        self.vacinas.append({"vacina": vacina, "data": data, "veterinario": veterinario, "crv": crv})

    def adicionar_doenca(self, doenca, data):
        self.historico_doencas.append({"doenca": doenca, "data": data})

    def adicionar_medicamento(self, medicamento, data_inicio, data_fim):
        self.medicamentos.append({"medicamento": medicamento, "data_inicio": data_inicio, "data_fim": data_fim})

    def mostrar_carteira(self):
        print(f"Carteira de Vacinação de {self.nome} ({self.tipo}):")
        for vacina in self.vacinas:
            print(f"Vacina: {vacina['vacina']}, Data: {vacina['data']}, Veterinário: {vacina['veterinario']}, CRV: {vacina['crv']}")
        print("\nHistórico de Doenças:")
        for doenca in self.historico_doencas:
            print(f"Doença: {doenca['doenca']}, Data: {doenca['data']}")
        print("\nMedicamentos Utilizados:")
        for medicamento in self.medicamentos:
            print(f"Medicamento: {medicamento['medicamento']}, Início: {medicamento['data_inicio']}, Fim: {medicamento['data_fim']}")

# Função principal
def main():
    pets = []

    while True:
        print("\n1. Adicionar novo pet")
        print("2. Adicionar vacina")
        print("3. Adicionar doença")
        print("4. Adicionar medicamento")
        print("5. Mostrar carteira de vacinação")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do pet: ")
            tipo = input("Tipo do pet (cão/gato): ")
            pets.append(Pet(nome, tipo))
        elif escolha == "2":
            nome = input("Nome do pet: ")
            for pet in pets:
                if pet.nome == nome:
                    vacina = input("Nome da vacina: ")
                    data = input("Data da vacina (dd/mm/aaaa): ")
                    veterinario = input("Nome do veterinário: ")
                    crv = input("CRV do veterinário: ")
                    pet.adicionar_vacina(vacina, data, veterinario, crv)
                    break
            else:
                print("Pet não encontrado.")
        elif escolha == "3":
            nome = input("Nome do pet: ")
            for pet in pets:
                if pet.nome == nome:
                    doenca = input("Nome da doença: ")
                    data = input("Data da doença (dd/mm/aaaa): ")
                    pet.adicionar_doenca(doenca, data)
                    break
            else:
                print("Pet não encontrado.")
        elif escolha == "4":
            nome = input("Nome do pet: ")
            for pet in pets:
                if pet.nome == nome:
                    medicamento = input("Nome do medicamento: ")
                    data_inicio = input("Data de início (dd/mm/aaaa): ")
                    data_fim = input("Data de término (dd/mm/aaaa): ")
                    pet.adicionar_medicamento(medicamento, data_inicio, data_fim)
                    break
            else:
                print("Pet não encontrado.")
        elif escolha == "5":
            nome = input("Nome do pet: ")
            for pet in pets:
                if pet.nome == nome:
                    pet.mostrar_carteira()
                    break
            else:
                print("Pet não encontrado.")
        elif escolha == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
1
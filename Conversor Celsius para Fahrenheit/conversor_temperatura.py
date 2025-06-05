def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = ((fahrenheit - 32) / 1.8)
    return celsius

def menu():
    while True:
        print('\n*** Conversor de Temperatura ***')
        print('\n1 - Celsius para Fahrenheit')
        print('2 - Fahrenheit para Celsius')
        print('3 - Sair')

        escolha = input('\nEscolha uma opção: ')

        if escolha == '1':
            try:
                celsius = float(input('Digite a temperatura em Cº: '))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f'A temperatura em Fº é: {fahrenheit:.1f}')
            except ValueError:
                print('Por favor, digite um valor válido.')

        elif escolha == '2':
            try:
                fahrenheit = float(input('Digite a temperatura em Fº: '))
                celsius = fahrenheit_para_celsius(fahrenheit)
                print(f'A temperatura em Cº é: {celsius:.1f}')
            except ValueError:
                print('Por favor, digite um valor válido.')

        elif escolha == '3':
            print('Encerrando programa...')
            break

        else:
            print('Opção inválida.')

menu()
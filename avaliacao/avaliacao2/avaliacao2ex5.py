#conta bancaria

saldoi = float(input("Introduza o valor da sua conta bancaria: "))

operacao = float(input("Introduza o valor que quer creditar/debitar: "))

if operacao > 0:
    saldof = saldoi + operacao
    print("Credito realizado com sucesso (saldo apos operacao: {})".format(saldof))
elif operacao < 0:
    if -operacao > saldoi:
        print("Nao foi possivel completar o debito (saldo insuficiente)")
    else:
        saldof = saldoi + operacao
        print("Debito realizado com sucesso (saldo apos operacao: {})".format(saldof))
else:
    print("Nenhuma operacao foi realizada uma vez que o valor a creditar ou debitar e 0.")

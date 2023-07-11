def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    if saldo > 0:
        print(f"\nSaldo:\t\tR$ {saldo:.2f}\t(+)")
    elif saldo == 0:
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    else:
        print(f"\nSaldo:\t\tR$ {saldo:.2f}\t(-)")
    print("==========================================")

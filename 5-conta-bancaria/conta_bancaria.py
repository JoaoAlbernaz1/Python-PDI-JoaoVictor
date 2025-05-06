

class ContaBancaria:
   
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self._saldo = float(saldo_inicial)

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor

    def consultar_saldo(self) -> float:
        return self._saldo


def formatar_moeda(valor: float) -> str:
  
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


if __name__ == "__main__":
    conta = ContaBancaria("João Victor", 1000)

    print("Saldo inicial:", formatar_moeda(conta.consultar_saldo()))

    conta.depositar(500)
    print("Após depósito:", formatar_moeda(conta.consultar_saldo()))

    conta.sacar(300)
    print("Após saque:", formatar_moeda(conta.consultar_saldo()))

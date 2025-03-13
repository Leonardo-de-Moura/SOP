from collections import deque

class SjfScheduler:
    def __init__(self):
        self.fila_processos = deque()  

    def adicionar_processo(self, pid, tempo_exec):
        """Adiciona um novo processo à fila."""
        self.fila_processos.append((pid, tempo_exec))

    def sjf_scheduling(self):
        """
        Simula o escalonamento SJF.
        """
       
        self.fila_processos = deque(sorted(self.fila_processos, key=lambda x: x[1]))

        tempo_atual = 0
        tempos_espera = {}
        tempos_retorno = {}

        print("\nExecução dos processos na ordem SJF:\n")

        while self.fila_processos:
            pid, tempo_exec = self.fila_processos.popleft()  

            tempos_espera[pid] = tempo_atual 
            tempos_retorno[pid] = tempo_atual + tempo_exec  

            print(f"Processo {pid} executando... (Tempo: {tempo_atual} → {tempo_atual + tempo_exec})")

            tempo_atual += tempo_exec  

        print("\nResumo do escalonamento:")
        print("PID | Tempo de Espera | Tempo de Retorno")
        for pid in tempos_espera:
            print(f"{pid:^3} | {tempos_espera[pid]:^15} | {tempos_retorno[pid]:^14}")


scheduler = SjfScheduler()

scheduler.adicionar_processo(1, 5)
scheduler.adicionar_processo(2, 3)
scheduler.adicionar_processo(3, 8)
scheduler.adicionar_processo(4, 6)

scheduler.sjf_scheduling()
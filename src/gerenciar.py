
from rich.table import Table
from rich.console import Console

class Task:
    def __init__(self, id, tarefa):
        self.id = id
        self. tarefa = tarefa
    
    def getId(self):
        return self.id

    def getTarefa(self):
        return self.tarefa
    
class Gerenciar(Task):
    def __init__(self, horas, id, tarefa):
        self.listg = []
        super().__init__(id, tarefa)
        self.listg.append([horas, id, tarefa])
        
    def add_Task(self, horas, id, tarefa):
        self.listg.append([horas, id, tarefa])
        
    def show_List(self):
        table = Table(title='Lista de Tarefas')
        table.add_column("Horas",style="magenta")
        table.add_column("Id",style="magenta")
        table.add_column("Tarefa",style="magenta")
        console = Console()
        
        for li in self.listg:    
            table.add_row(str(li[0]), str(li[1]), str(li[2]))
        console.print(table)
        
    def remove_Task(self, id):
        i = 1
        nlist = []
        for nli in self.listg:
            if int(nli[1]) != int(id):
                nlist.append([nli[0], i, nli[2]])
                i+=1
        self.listg.clear()
        self.listg = nlist
                
ta = Gerenciar('06:00',1,'Acordar e tomar café')
ta.add_Task('10:30',2,'Tomar remedio')
ta.add_Task('11:00',3,'Almoçar')
ta.add_Task('17:40',4,'Me preparar para o final')

ta.show_List()
ta.remove_Task(3)
ta.show_List()

ta.remove_Task(2)
ta.show_List()

# Gerenciador de Tarefas ⏰

Um simples gerenciador de tarefas em Python que utiliza a biblioteca **Rich** para exibir uma lista organizada e colorida de tarefas no terminal.  
Permite adicionar, remover e visualizar tarefas com horários definidos.

---

## 🚀 Funcionalidades
- Adicionar novas tarefas com horário, ID e descrição.
- Remover tarefas pelo ID.
- Exibir todas as tarefas em uma tabela estilizada.
- IDs são reorganizados automaticamente após remoção.

---

## 📦 Tecnologias utilizadas
- **Python 3**
- [Rich](https://github.com/Textualize/rich) – para exibição estilizada no terminal

---

## 📖 Exemplo de uso

```python
from task import Task
from rich.table import Table
from rich.console import Console

# Criando o gerenciador
ta = Gerenciar('06:00', 1, 'Acordar e tomar café')

# Adicionando tarefas
ta.add_Task('10:30', 2, 'Tomar remédio')
ta.add_Task('11:00', 3, 'Almoçar')
ta.add_Task('17:40', 4, 'Me preparar para o final do dia')

# Exibindo lista
ta.show_List()

# Removendo tarefas
ta.remove_Task(3)
ta.show_List()

git clone https://github.com/seu-usuario/gerenciador-tarefas.git
cd gerenciador-tarefas
pip install rich

Desenvolvido por Marco Aurélio

📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.
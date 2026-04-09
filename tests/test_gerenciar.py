import unittest
from src.gerenciar import Gerenciar

class TestGerenciar(unittest.TestCase):
    def setUp(self):
        # Criando uma instância inicial
        self.ger = Gerenciar("06:00", 1, "Acordar e tomar café")
        self.ger.add_Task("10:30", 2, "Tomar remédio")
        self.ger.add_Task("11:00", 3, "Almoçar")

    def test_add_task(self):
        self.ger.add_Task("17:40", 4, "Me preparar para o final")
        self.assertEqual(len(self.ger.listg), 4)
        self.assertEqual(self.ger.listg[-1][2], "Me preparar para o final")

    def test_remove_task(self):
        self.ger.remove_Task(2)
        tarefas = [t[2] for t in self.ger.listg]
        self.assertNotIn("Tomar remédio", tarefas)
        self.assertEqual(len(self.ger.listg), 2)


    def test_show_list(self):
        # Apenas verifica se o método não gera erro
        try:
            self.ger.show_List()
        except Exception as e:
            self.fail(f"show_List gerou exceção: {e}")

if __name__ == "__main__":
    unittest.main()

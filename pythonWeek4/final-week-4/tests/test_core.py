import unittest
from taskmanager import core

class TestTaskManager(unittest.TestCase):

    def setUp():
        core.DB_NAME = ":memory:"
        core.init_db()

    def test_add_task(self):
        core.add_task("Test Task")
        tasks = core.list_tasks()
        self.assertEquals(len(tasks), 1)
        self.assertEquals(tasks[0][1], "Test Task")
    
if __name__ == "__main__":
    unittest.main()
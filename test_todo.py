# Student Name: Ricardo Danganan Jnr
# Student ID: X00191395
# Module: DevOps - Continuous Integration and Deployment
# Created on: 20/11/2024
# This file contains the unit tests for the todo app using the unittest module in Python.

# Import the unittest module
import unittest
from todo import tasks, add_task, view_tasks, mark_task, delete_task

# Create a test class that inherits from unittest.TestCase
class TestTodoApp(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        add_task("Test Task")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], "Test Task")
        self.assertFalse(tasks[0]['completed'])

    def test_mark_task_complete(self):
        add_task("Another Task")
        mark_task(0, completed=True)
        self.assertTrue(tasks[0]['completed'])

    def test_mark_task_incomplete(self):
        add_task("Yet Another Task")
        mark_task(0, completed=False)
        self.assertFalse(tasks[0]['completed'])

    def test_delete_task(self):
        add_task("Task to Delete")
        delete_task(0)
        self.assertEqual(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()

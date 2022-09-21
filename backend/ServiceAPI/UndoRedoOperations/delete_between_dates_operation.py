from django.db import models
from .undo_redo_operation import UndoRedoOperation


class DeleteBetweenDatesOperation(UndoRedoOperation):
    def __init__(self, to_be_deleted: list[(models.Model, int)]):
        self.to_be_deleted = to_be_deleted

    def undo(self):
        for transaction in self.to_be_deleted:
            transaction[0].pk = transaction[1]
            transaction[0].save()

    def redo(self):
        for transaction in self.to_be_deleted:
            transaction[0].delete()

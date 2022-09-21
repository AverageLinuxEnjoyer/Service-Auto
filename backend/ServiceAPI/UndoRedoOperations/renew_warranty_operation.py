from django.db import models
from .undo_redo_operation import UndoRedoOperation


class WarrantyOperation(UndoRedoOperation):
    def __init__(self, cars_with_renewed_warranty):
        self.cars_with_renewed_warranty = cars_with_renewed_warranty

    def undo(self):
        for car in self.cars_with_renewed_warranty:
            car.warranty = False
            car.save()

    def redo(self):
        for car in self.cars_with_renewed_warranty:
            car.warranty = True
            car.save()

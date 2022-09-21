from ..UndoRedoOperations.delete_operation import DeleteOperation
from ..service.undo_redo_service import UndoRedoService

from typing import Callable


def delete_undo_redo(function: Callable):
    def wrapper(*args, **kwargs):

        if "undoredo" not in kwargs or kwargs["undoredo"] is True:
            if "id" in kwargs:
                id = kwargs["id"]

        deleted_object = function(*args, **kwargs)

        if "undoredo" not in kwargs or kwargs["undoredo"] is True:
            UndoRedoService.addUndoOperation(
                DeleteOperation(id, deleted_object))
            UndoRedoService.clear_redo()

        return deleted_object

    return wrapper

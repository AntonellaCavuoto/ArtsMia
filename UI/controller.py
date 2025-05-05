import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(
            f"Grafo creato. Il grafo contiene {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi"
        ))

        self._view._txtIdOggetto.disabled = False
        self._view._btnCompConnessa.disabled = False

        self._view.update_page()

    def handleCompConnessa(self, e):
        txtInput = self._view._txtIdOggetto.value

        if txtInput == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire id", color = "red"))
            self._view.update_page()
            return

        try:
            idInput = int(txtInput)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un numero", color="red"))
            self._view.update_page()
            return

        if not self._model.hasNode(idInput):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("L'id inserito non corrisponde a un nodo del grafo", color="red"))
            self._view.update_page()
            return

        sizeCompConnessa = self._model.getInfoConnessa(idInput)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene "
                                                     f"il nodo {self._model.getObjectFromId(idInput)} "
                                                     f"ha dimensione pari a {sizeCompConnessa}"))
        self._view.update_page()







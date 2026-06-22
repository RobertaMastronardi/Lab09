import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        dist_min=self._view._txtInDistanzaMin.value
        if dist_min=="":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Per favore inserisci un valore di distanza", color="red"))
            self._view.update_page()
            return
        try:
            dist_min_f=float(dist_min)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico di distanza", color="red"))
            self._view.update_page()
            return
        self._model.buildGraph(dist_min_f)
        n, e=self._model.getGraphDetails()
        archi=self._model.getAllEdges()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Grafo correttamente creato. Il grafo possiede {n} nodi e {e} archi.'))
        for a in archi:
            self._view.txt_result.controls.append(ft.Text(f'{a[0]} -- {a[1]} | peso: {a[2]}'))
        self._view.update_page()

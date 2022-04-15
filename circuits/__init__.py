from PySpice.Spice.Netlist import Circuit as PySpiceCircuit

from configuration import skywater_configuration
from services.LoadExternalLibrary import LoadExternalLibraryService


class Circuit(PySpiceCircuit):
    def __init__(self, title: str, ground=0, *args, **kwargs):
        super().__init__(title, ground, *args, **kwargs)

        for library in skywater_configuration.libraries:
            LoadExternalLibraryService.execute(self, library)

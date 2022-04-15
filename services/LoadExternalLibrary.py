from PySpice.Spice.Netlist import Circuit


class LoadExternalLibraryService:
    @staticmethod
    def execute(circuit: Circuit, library_path: str) -> None:
        circuit.include(library_path)

from flask import Flask, request, jsonify

from configuration import skywater_configuration
from services.ExtractSParameters import ExtractSParametersService
from subCircuits.LNA import LNASubCircuit
from subCircuits.RLC import RLCSubCircuit


app = Flask(__name__)


@app.route("/RLC", methods=["POST"])
def simulate_rlc():
    body_request = request.json
    rlc = RLCSubCircuit(
        name="rlcSubCircuit",
        capacitance=body_request["c"],
        inductance=body_request["l"],
        resistance=body_request["r"],
    )

    try:
        s_parameters = ExtractSParametersService.execute(
            rlc,
            start_frequency=body_request["startFrequency"],
            stop_frequency=body_request["stopFrequency"],
            number_of_points=int(body_request["simulationPoints"]),
            variation=body_request["simulationVariation"],
        )
    except Exception as exception:
        print(exception)
        return jsonify({"error": True})
    return (
        jsonify(
            {
                "frequency": s_parameters.frequency.tolist(),
                "S11": s_parameters.S11_db.tolist(),
                "S12": s_parameters.S12_db.tolist(),
                "S21": s_parameters.S21_db.tolist(),
                "S22": s_parameters.S22_db.tolist(),
                "error": False,
            }
        ),
        201,
    )


@app.route("/", methods=["POST"])
def hello_world():
    body_request = request.json

    lna = LNASubCircuit(
        "lnaSubCircuit",
        skywater_configuration.nfet_type,
        skywater_configuration.pfet_type,
        c1=body_request["c1"],
        l1=body_request["l1"],
        l2=body_request["l2"],
        lg=body_request["lg"],
        rf=body_request["rf"],
        rpol1=body_request["rpol1"],
        vpol1=body_request["vpol1"],
        w1=body_request["w1"],
        w2=body_request["w2"],
        lpk=body_request["lpk"],
        cm2=body_request["cm2"],
        cm1=body_request["cm1"],
        l3=body_request["l3"],
        rpol2=body_request["rpol2"],
        vpol2=body_request["vpol2"],
        w3=body_request["w3"],
        cm3=body_request["cm3"],
        vdd=body_request["vdd"],
        vcc=body_request["vcc"],
    )

    try:
        s_parameters = ExtractSParametersService.execute(
            lna,
            start_frequency=body_request["startFrequency"],
            stop_frequency=body_request["stopFrequency"],
            number_of_points=int(body_request["simulationPoints"]),
            variation=body_request["simulationVariation"],
        )
    except Exception as exception:
        print(exception)
        return jsonify({"error": True})
    return (
        jsonify(
            {
                "frequency": s_parameters.frequency.tolist(),
                "S11": s_parameters.S11_db.tolist(),
                "S12": s_parameters.S12_db.tolist(),
                "S21": s_parameters.S21_db.tolist(),
                "S22": s_parameters.S22_db.tolist(),
                "error": False,
            }
        ),
        201,
    )

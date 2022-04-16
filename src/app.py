from flask import Flask, request, jsonify

from configuration import skywater_configuration
from services.ExtractSParameters import ExtractSParametersService
from subCircuits.LNA import LNASubCircuit


app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    body_request = request.json

    lna = LNASubCircuit(
        "lnaSubCircuit",
        skywater_configuration.nfet_type,
        skywater_configuration.pfet_type,
        vpol2=body_request["vpol2"],
        cm3=body_request["cm3"],
        c1=body_request["c1"],
        cdec=body_request["cdec"],
        cm1=body_request["cm1"],
        cm2=body_request["cm2"],
        l1=body_request["l1"],
        l2=body_request["l2"],
        l3=body_request["l3"],
        lg=body_request["lg"],
        lpk=body_request["lpk"],
        rf=body_request["rf"],
        rpol1=body_request["rpol1"],
        rpol2=body_request["rpol2"],
        vpol1=body_request["vpol1"],
        w1=body_request["w1"],
        w2=body_request["w2"],
        w3=body_request["w3"],
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

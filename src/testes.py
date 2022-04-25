from matplotlib import pyplot as plt
from configuration import skywater_configuration
from services.ExtractSParameters import ExtractSParametersService
from subCircuits.LNA import LNASubCircuit

test_subcircuit = LNASubCircuit(
    "test",
    nfet_type=skywater_configuration.nfet_type,
    pfet_type=skywater_configuration.pfet_type,
    c1=1.760011623829603e-11,
    cdec=1e-6,
    cm1=1.7124060225486756e-11,
    cm2=1.8947868962883948e-11,
    cm3=5.416065746545791e-13,
    l1=35.25476063966751,
    l2=32.957107959985734,
    l3=38.06572427272797,
    lg=5.53381922841072e-10,
    lpk=7.58953581303358e-09,
    rf=65736.40324175358,
    rpol1=92193.67206096649,
    rpol2=35182.76825547218,
    vpol1=0.8043120324611663,
    vpol2=1.6785887360572815,
    w1=93.52270918190479,
    w2=10.99694906949997,
    w3=91.55357965350152,
)
s_parameters = ExtractSParametersService.execute(test_subcircuit, 1, 3e9, 1000)


plt.subplot(2, 2, 1)
plt.plot(s_parameters.frequency, s_parameters.S11_db, label="S11")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 2)
plt.plot(s_parameters.frequency, s_parameters.S12_db, label="S12")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 3)
plt.plot(s_parameters.frequency, s_parameters.S21_db, label="S21")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 4)
plt.plot(s_parameters.frequency, s_parameters.S22_db, label="S22")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.tight_layout()
plt.show()

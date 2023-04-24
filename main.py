import gdsfactory as gf
import matplotlib.pyplot as plt
import sky130
from gdsfactory.generic_tech import get_generic_pdk

gf.config.rich_output()

PDK = get_generic_pdk()
PDK.activate()

c = gf.Component(name="NOT from 2 NAND gates")

nand1 = c << sky130.components.sky130_fd_sc_hd__nand2_2()
nand2 = c << sky130.components.sky130_fd_sc_hd__nand2_2()

nand2.move((20, 20))

route = gf.routing.get_route_electrical(nand1.ports['VPWR1'], nand2.ports['VPWR1'], radius=0.1)
c.add(route.references)

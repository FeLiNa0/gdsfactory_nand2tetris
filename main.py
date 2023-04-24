import gdsfactory as gf
import matplotlib.pyplot as plt
import sky130
from gdsfactory.generic_tech import get_generic_pdk

# TODO Turn on debug logging
gf.config.rich_output()

PDK = sky130.PDK

c = gf.Component(name="2 NAND connected gates")

# high voltage (5V), 2_1
# sky130.components.sky130_fd_sc_hvl__nand2_1()
# high density, 2_2
# sky130.components.sky130_fd_sc_hd__nand2_2()

# Create reference to two NAND gates
nand1 = c << sky130.components.sky130_fd_sc_hd__nand2_2()
nand2 = c << sky130.components.sky130_fd_sc_hd__nand2_2()

nand2.move(nand1.get_bounding_box()[1])
nand2.move((1, 1))

# took forever to find 'strip', I tried 'metal1' and the default 'metal_section' too
# I tried the generic PDK and an empty PDK by accident from sky130.Pdk(?), I used sky130.PDK instead
route = gf.routing.get_route_electrical(nand1.ports['VPWR'], nand2.ports['VPWR'], cross_section='strip')
c.add(route.references)

# Visualize with:
# c.to_3d().show()
# c.plot_matplotlib()
# c.plot_klayout()
# TODO add a c.plot_kweb() ?

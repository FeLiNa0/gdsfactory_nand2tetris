import matplotlib.pyplot as plt
import gdsfactory as gf
import sky130

# probably wrong
c = sky130.components.sky130_fd_sc_hd__nand2_2()

c2 = sky130.components.sky130_fd_sc_hd__nand2_2()
pc2 = c2 << gf.components.pad_array(orientation=270, columns=3)
route = gf.routing.get_route_electrical(c.ports['VPWR'], pc2.ports['VPWR1'])
c.add(route.references)

pc2.plot_matplotlib()
plt.show()

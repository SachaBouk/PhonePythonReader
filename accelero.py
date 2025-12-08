import math

window = None
document = None

def create_proxy(func):
    pass

class AccelSensor:
    def get_xyz(self):
        xyz = window.getAccelXYZ()
        x = float(xyz[0] or 0.0)
        y = float(xyz[1] or 0.0)
        z = float(xyz[2] or 0.0)
        return x, y, z

    def get_magnitude(self):
        x, y, z = self.get_xyz()
        return math.sqrt(x*x + y*y + z*z)
    
    def get_SmartphoneState(self):
        x, y, z = self.get_xyz()
        if abs(x) > abs(y):
            if x > 0:
                return "RIGHT"
            else:
                return "LEFT"
        else:
            if y > 0:
                return "UP"
            else:
                return "DOWN"

accel = AccelSensor()

def update(*args, **kwargs):
    x, y, z = accel.get_xyz()
    m = accel.get_magnitude()
    document.getElementById("values").innerText = (
        f"x={x:.2f}, y={y:.2f}, z={z:.2f}, |a|={m:.2f}, SmartphoneState={accel.get_SmartphoneState()}"
    )
    window.addAccelPoint(x, y, z)

update_proxy = create_proxy(update)
window.setInterval(update_proxy, 200)

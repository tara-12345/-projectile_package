import matplotlib.pyplot as plt
from numpy import sign

def update_state(t, x, v, a, dt=0.1):
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt

    x += distance_moved
    
    return t, x, v

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_air+force_gravity
    a = total_force/mass
    
    return a

def calculate_acceleration_x(v, k=0.0, mass=1.0):
    
    force_air = -sign(v)*k*v**2
    a = force_air/mass
    
    return a


def flying_mass(vy, vx, k=0.0, mass=1.0, dt=0.1):
    gravity = -9.81 # m/s2
    initial_height = 0.0

    # Initial values for our parameters
    distance_moved = 0
    y = initial_height
    vy = vy
    t = 0.0
    x = 0.0
    a_x = 0.0
    a_y = 0.0
    vx = vx
    
    # Create empty lists which we will update
    height = []
    velocity = []
    time = []
    x_coords = []
    velocity_x = []

      # Keep looping while the object is still falling
    while y >= 0:
        a_x = calculate_acceleration_x(vx, k=k, mass=mass)
        a_y = calculate_acceleration_y(vy, k=k, mass=mass, gravity=gravity)

        # Append values to list and then update
        height.append(y)
        velocity.append(vy)
        time.append(t)
        x_coords.append(x)
        velocity_x.append(vx)
        

        # Update the state for time, height and velocity
        t, y, vy = update_state(t, y, vy, a_y, dt=dt)
        t, x, vx = update_state(t, x, vx, a_x, dt=dt)
        
    
    return time, x_coords, height, velocity_x, velocity

   
    
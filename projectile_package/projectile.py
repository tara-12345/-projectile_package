def update_state(t, x, v, a, dt=0.1):
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt

    x += distance_moved
    
    return t, x, v

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_air
    a = total_force/mass
    
    return a

def calculate_acceleration_x(v, k=0.0, mass=1.0, gravity=-9.81):
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a = total_force/mass
    
    return a


def flying_mass(v, vx, k=0.0, mass=1.0, dt=0.1):
    start_velocity = 0.0 # m/s
    gravity = -9.81 # m/s2

    # Initial values for our parameters
    distance_moved = 0
    y = initial_height
    v = start_velocity
    t = 0.0
    x = 0.0
    a_x = 0.0
    a_y = 0.0
    vx = start_velocity
    
    # Create empty lists which we will update
    height = []
    velocity = []
    time = []
    x_coords = []
    
      # Keep looping while the object is still falling
    while h > 0:
        a_x = calculate_acceleration_x(v, k=k, mass=mass, gravity=gravity)
        a_y = calculate_acceleration_y(v, k=k, mass=mass, gravity=gravity)

        # Append values to list and then update
        height.append(y)
        velocity.append(v)
        time.append(t)
        x_coords.append(x)
        
        # Update the state for time, height and velocity
        t, y, v = update_state(t, h, v, a, dt=dt)
        t, x, vx = update_state(t, h, v, a, dt=dt)
        
    
    return t, x, y, vx, v

   
    
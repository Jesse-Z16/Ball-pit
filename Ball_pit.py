# Ball pit program

# -------------------------
# Subprograms
# -------------------------
# Function to return the volume of the ball pit
def ball_pit_volume(ball_pit_radius, ball_pit_height):
    pi = 3.14
    return pi * (ball_pit_radius * ball_pit_radius) * ball_pit_height


# Function to return the volume of a ball
def ball_volume(ball_radius):
    pi = 3.14
    return (4 / 3) * pi * (ball_radius * ball_radius * ball_radius)


# -------------------------
# Main program
# -------------------------
ball_pit_radius = 1  # Meters
ball_pit_height = 0.2  # Meters
ball_radius = 0.05  # Meters
packing_density = 0.75  # Volume taken up by the balls
balls = (ball_pit_volume(ball_pit_radius, ball_pit_height) / ball_volume(ball_radius)) * packing_density
print("You need", balls, "balls to fill the ball pit.")

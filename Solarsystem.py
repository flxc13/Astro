import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67428e-11  # Gravitational constant
AU = 1.496e11  # Astronomical unit (distance from the Earth to the Sun)


# Class representing a planet
class Planet:
    def __init__(self, name, distance, period, color):
        self.name = name
        self.distance = distance * AU
        self.period = period
        self.color = color
        self.angle = 0
        self.speed = 2 * np.pi / period  # angular speed in radians/day
        self.x = self.distance
        self.y = 0


# Initialize planets with their distance from the Sun in AU and orbital period in Earth days
planets = [
    Planet("Mercury", 0.387, 88, 'darkgrey'),
    Planet("Venus", 0.723, 224.7, 'yellow'),
    Planet("Earth", 1, 365.25, 'blue'),
    Planet("Mars", 1.524, 687, 'red'),
    Planet("Jupiter", 5.204, 4333, 'orange'),
    Planet("Saturn", 9.582, 10759, 'gold'),
    Planet("Uranus", 19.201, 30687, 'lightblue'),
    Planet("Neptune", 30.047, 60190, 'darkblue')
]

# Setup the plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-35 * AU, 35 * AU)
ax.set_ylim(-35 * AU, 35 * AU)
sun = plt.Circle((0, 0), 0.1 * AU, color='yellow', label='Sun')
ax.add_artist(sun)

# Create plot elements that will be updated
orbits = []
dots = []
for planet in planets:
    orbit, = ax.plot([], [], color=planet.color, linewidth=1.0, label=planet.name)
    dot, = ax.plot([], [], 'o', color=planet.color)
    orbits.append(orbit)
    dots.append(dot)


# Function to update the plot for each frame
def update(frame):
    for i, planet in enumerate(planets):
        planet.angle += frame / planet.period * 2 * np.pi

        # Update the positions
        planet.x = planet.distance * np.cos(planet.angle)
        planet.y = planet.distance * np.sin(planet.angle)

        # Update the orbits and current positions
        orbits[i].set_data([planet.distance * np.cos(angle) for angle in np.linspace(0, 2 * np.pi, 300)],
                           [planet.distance * np.sin(angle) for angle in np.linspace(0, 2 * np.pi, 300)])
        dots[i].set_data(planet.x, planet.y)

    return orbits + dots


# Initialize the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 365, 365), blit=True, repeat=True, interval=7)

# Add a legend
ax.legend(loc="lower left", bbox_to_anchor=(1.05, 0))

# Show the plot
plt.show()

#Lauren Song
#U79789182
#Using Newton’s Law of Universal Gravitation

#The following values are from NASA
#Store values in scientific notation

g = 6.672e-11 # Gravitational constant, G (in Nm2 kg-2)
mass_sun = 1.988500e30 # Mass of the sun (in kilograms)
mass_earth = 5.9724e24 # Mass of the earth (in kilograms)
mass_moon = 7.346e22 # Mass of the moon (in kilograms)
distance_sun_earth = 1.4966862e11 # Distance between the sun and the earth (in meters)
distance_moon_earth = 3.844e8 # Distance between the moon and the earth (in meters
distance_sun_moon = 1.5e11 #Distance between the sun and moon (in meters)


#Compute F = G * ((m1 * m2)/ r**2))

#a)The Force exerted by the Sun on the Moon
Force = g * ((mass_sun * mass_moon) / (distance_sun_moon**2))
print('The Force exerted by the Sun on the Moon:', Force, 'Newton')

#b)The Force exerted by the Earth on the Moon
Force = g * ((mass_earth * mass_moon) / (distance_moon_earth**2))
print('The Force exerted by the Earth on the Moon:', Force, 'Newton')

#c)The Force exerted by the Sun on the Earth
Force = g * ((mass_sun * mass_earth) / (distance_sun_earth**2))
print('The Force exerted by the Sun on the Earth:', Force, 'Newton')

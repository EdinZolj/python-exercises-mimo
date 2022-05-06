# Using string comparisons to lable survey data and gain insights about the fitness apps users.
# Cecking users survey answers regarding activity frequency and intensity, label them, and display the results.

frequency = "once a week"
intensity = "low"

highly_active = frequency == "dail"
print("Highly active user:")
print(highly_active)

highly_intensity = intensity == "high"
print("high intensity sports:")
print(highly_intensity)
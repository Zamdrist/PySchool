# Calculate paycheck based on regular hours and rate plus over time hours and rate
#
regularHours = 40
regularRate = 15.34
overtimeHours = 10
overtimeRate = regularRate * 1.5

print("Your will be paid $" +
      str((regularRate * regularHours) +
          (overtimeRate * overtimeHours)),
      "this week")
"""
Traffic Light System
Problem Statement

Display action based on traffic light color.

Rules:
Red → Stop
Yellow → Get Ready
Green → Go
Else → Invalid color
"""

color = input("Enter traffic light color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

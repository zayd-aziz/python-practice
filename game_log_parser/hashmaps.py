# Create a hashmap (dictionary) of player -> points
points = {
    "Mahomes": 24.5,
    "Jefferson": 18.2,
    "McCaffrey": 27.1,
}

# Add or update
points["Chase"] = 21.0        # add a new key
points["Mahomes"] = 26.0      # overwrite an existing key

# Look up
print(points["McCaffrey"])            # 27.1
print(points.get("Kelce", 0))         # 0 (safe lookup with a default)

# Check if a key exists
if "McCaffrey" in points:
    print("McCaffrey is on the roster")

# Delete
del points["McCaffrey"]

# Loop over it
for player, pts in points.items():
    print(f"{player}: {pts}")

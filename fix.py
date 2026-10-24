import os
# 1.1 se 6.5 tak ke folders dhoondo
for name in os.listdir("."):
    if os.path.isdir(name) and (name.startswith("Assignment-1.") or name.startswith("Assignment-2.") or name.startswith("Assignment-3.") or name.startswith("Assignment-4.") or name.startswith("Assignment-5.") or name.startswith("Assignment-6.")):
        a = os.path.join(name, "assignment.md")
        b = os.path.join(name, "index.md")
        if os.path.exists(a) and os.path.exists(b):
            print(f"Fixing {name}")
            t = os.path.join(name, "temp.md")
            os.rename(a, t)
            os.rename(b, a)
            os.rename(t, b)
print("Done ho gaya!")

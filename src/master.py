import subprocess

# List of Python scripts to run in sequence
scripts = [
    "src/dc.py",
    "src/pre.py",
    "src/model_building.py",
    "src/evaluation.py"

]

# Run each script
for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)  # Output of the script
    if result.returncode != 0:
        print(f"Error in {script}: {result.stderr}")
        break

import sea_level_predictor
from unittest import main
import datetime

print("Programmer: Mamoudou T. Bah")
time = datetime.datetime.now()
print(f"Seal Level Data, {time.strftime('%B %d, %Y @ %H:%M:%S')}")
print("")

# Test your function by calling it here
sea_level_predictor.draw_plot()

# Run unit tests automatically
main(module='test_module', exit=False)
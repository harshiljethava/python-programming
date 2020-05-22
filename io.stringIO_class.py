import sys
import io
print(io.StringIO())
print("An error message",file=sys.stdout)
sys.stdout.write("New error message")
sys.stdout.write=io.StringIO()
"""
sys.stdout.write=io.StringIO()

print("An error message ",end="",file=sys.stdout)
sys.stdout.write("Another error message")
"""

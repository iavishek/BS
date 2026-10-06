import sys
print("Welcome Everyone !!")
print("First parameter", type(sys.argv[1]))
print("Second parameter", type( sys.argv[2]))

## Commands to run ##
# python hello.py 123 avi
# python hello.py 123 avi 78 i9 56 ju
## Result will be same based on parameter defined in function ##

print("First parameter type", sys.argv[1])
print("Second parameter type", sys.argv[2])
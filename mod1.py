import mod2
#now __name__ give mod2
import app
'''this will execute the entire code inside app module hence,
if __name__ == "__main__":
    app.run(debug=True)  we write this code inside app.py, since __name__ will not be main if mod1 was run''' 

print(f"Running module 1 - ({__name__})")
                           #value of name is "__main__" if code is run this scope only
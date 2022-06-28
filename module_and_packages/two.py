import module_and_packages.one as one

print("TOP LEVEL IN TWO.Py")

one.func()

if __name__ == '__main__':
    print('TWO.PY IS being run directly')

else:  
    print('TWO.PY has been imported!')
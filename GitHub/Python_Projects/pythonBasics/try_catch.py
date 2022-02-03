
def getInfo():
    var1 = input('provide a numeric value: ')
    var2 = input('provide a second numeric value: ')
    return var1, var2

def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            print("{} + {} = {}".format(var1, var2, var3))
            go = False
        except ValueError:
            print('input a valid number')
        except:
            print('wow you done messed up')
        
    

if __name__ == "__main__":
    compute()

#simple validation
def valid(v):
    if len(v) == 5:
        try:
            int(val)
            return "success"
        except:
            return "Not a digit"
    elif len(v) <= 5:
        return "Less digits entered"
    elif len(v) >= 5:
        return "More digits entered"
    else:
        return "no digit"
if __name__ == "__main__":
    val = input("Enter the pin code : ")
    print(valid(val))
    
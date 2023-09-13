import utils

utilsObj = utils.utils()

# reversed
reversedInt = utilsObj.reversed(123)
if reversedInt == 321:
    print("Passed reversed int")
else:
    print("Failed reversed int")

reversedFloat = utilsObj.reversed(123.123)
if reversedFloat == 321:
    print("Passed reversed float")
else:
    print("Failed reversed float")

reversedString = utilsObj.reversed("123")
if reversedString == 321:
    print("Passed reversed string")
else:
    print("Failed reversed string")

# formatter
formatterIntBin, formatterIntOct = utilsObj.formatter(100)
if formatterIntBin == "1100100" and formatterIntOct == "144":
    print("Passed formatter int")
else:
    print("Failed formatter int")

formatterFloatBin, formatterFloatOct = utilsObj.formatter(100.123)
if formatterFloatBin == "1100100" and formatterFloatOct == "144":
    print("Passed formatter float")
else:
    print("Failed formatter float")

formatterStringBin, formatterStringOct = utilsObj.formatter("100")
if formatterStringBin == "1100100" and formatterStringOct == "144":
    print("Passed formatter string")
else:
    print("Failed formatter string")
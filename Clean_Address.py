def cleanJl(obj):
    if "JL." in obj: return obj.replace("JL.","Jl.")
    elif "Jalan " in obj: return obj.replace("Jalan ","Jl. ")
    elif "jl." in obj: return obj.replace("jl.","Jl.")
    elif "jln." in obj: return obj.replace("jln.","Jl.")
    elif "jalan " in obj: return obj.replace("jalan","Jl.")
    else: return obj

def checkNum(numCheck):

    if "nomor" in numCheck: return numCheck.replace("nomor","No")
    elif "No " in numCheck: return numCheck.replace("No ", "No. ")
    elif "NO." in numCheck: return numCheck.replace("NO","No")
    elif "NO " in numCheck: return numCheck.replace("NO","No.")
    elif "No," in numCheck: return numCheck.replace("No,","No.")
    elif "no." in numCheck: return numCheck.replace("no.", "No.")
    elif "Nomor" in numCheck: return numCheck.replace("Nomor","No. ")
    elif "NOMOR " in numCheck: return numCheck.replace("NOMOR ","No. ")
    elif "no " in numCheck: return checKno(numCheck)
    else: return numCheck

def checKno(num):
    if num.index("no ") == 0:
        return num.replace("no ","No. ")
    else: return num

def cleanNum(obj):

    if "No." in obj:
        objA = obj.replace("No.","No. ")
        if "  " in objA:
            result = objA.replace("  "," ")
        else:
            result = objA
    else: result = obj
    return result

def cleanGg(obj):
    if "Gg " in obj: return obj.replace("Gg ","Gg. ")
    elif "Gang" in obj: return obj.replace("Gang","Gg.")
    else: return obj

def cleanRT(obj):
    if " rt" in obj: return obj.replace(" rt"," RT")
    else: return obj

def cleanRW(obj):
    if " rw" in obj: return obj.replace(" rw"," RW")
    else: return obj

def cleanAddress(addressField):
    obj = addressField
    if "Jl." not in obj:
        if "Gg." in obj:
            if "," in obj:
                if obj.index("Gg.") == 0:
                    result = obj[:(obj.index(",")):].strip()
                elif obj.index("Gg.") > 0 and obj.index(",") < 4:
                    preresult = obj[obj.index("Gg.")::]
                    if "," in preresult:
                        result = preresult[:preresult.index(","):].strip()
                    else: result =preresult.strip()
                else:
                    preresultA = obj[:obj.index("Gg."):].strip()
                    preresultB = obj[obj.index("Gg.")::].strip()
                    if "," in preresultB:
                        preresultC = preresultB[:preresultB.index(","):].strip()
                        result = preresultA + " " + preresultC
                    else: result = obj
            else: result = obj
        else:
            if "RT" in obj and "," in obj:
                if obj.index("RT") < obj.index(",") and obj.index("RT") == 0:
                    preresult = obj[((obj.index(",")) + 1)::]
                    if "," in preresult:
                        result = preresult[:(preresult.index(",")):].strip()
                    else: result = preresult.strip()
                elif obj.index("RT") > obj.index(","):
                    if obj.index(",") < 4:
                        preresult = obj[obj.index(",")+1::].strip()
                        if "," in preresult:
                            if preresult.index("RT") < preresult.index(","):
                                preresultA = preresult[preresult.index(",")+1::].strip()
                                if "," in preresultA:
                                    result = preresultA[:preresultA.index(","):].strip()
                                else: result = preresultA.strip()
                            else: result = preresult.strip()
                        else: result = preresult.strip()
                    else: result = obj[:(obj.index(","))].strip()
                else: result = obj
            elif "RW" in obj and "," in obj:
                if obj.index("RW") < obj.index(",") and obj.index("RW") == 0:
                    preresult = obj[((obj.index(",")) + 1)::]
                    if "," in preresult:
                        result = preresult[:(preresult.index(",")):].strip()
                    else: result = preresult.strip()
                elif obj.index("RW") > obj.index(","):
                    result = obj[:(obj.index(","))].strip()
                else: result = obj
            else: result = obj
    else:
        if "," in obj:
            if obj.index("Jl") == 0:
                result = obj[:(obj.index(",")):].strip()
            elif obj.index("Jl") > 0 and obj.index(",") < 4:
                preresult = obj[obj.index("Jl")::]
                if "," in preresult:
                    result = preresult[:preresult.index(","):].strip()
                else: result =preresult.strip()
            elif obj.index("Jl") > 10 and obj.index(",") > obj.index("Jl"):
                preresultA = obj[:obj.index(","):].strip()
                preresultB = preresultA[:preresultA.index("Jl"):].strip()
                preresultC = preresultA[preresultA.index("Jl")::]
                result = preresultB + ", " + preresultC
            else:
                preresultA = obj[:obj.index("Jl"):].strip()
                preresultB = obj[obj.index("Jl")::].strip()
                if "," in preresultB:
                    preresultC = preresultB[:preresultB.index(","):].strip()
                    result = preresultA + " " + preresultC
                else: result = obj
        else: result = obj

    return secondCheck(result)

def secondCheck(result):

    if "No" in result and "Jl" in result and "," in result:
        if result.index("No") == 0:
            resultA = result[:result.index(","):].strip()
            resultB = result[result.index(",")+1::].strip()
            if "No" in resultB and "Jl" in resultB:
                if resultB[(resultB.index("No") + 4)] not in "1234567890":
                    resultC = resultB[:resultB.index("No"):].strip()
                    address = resultC + " " + resultA
                else:
                    address = resultB
            elif "Jl" in resultB and "No" not in resultB:
                address = resultB + " " + resultA
            else:
                address = result
        else:
            address = result
    elif "No" in result and "Jl" in result and "," not in result:
        if result.index("No") == 0:
            resultA = result[:result.index("Jl"):].strip()
            resultB = result[result.index("Jl")::].strip()
            if "No" in resultB:
                if resultB[(resultB.index("No") + 4)] not in "1234567890":
                    resultC = resultB[:resultB.index("No"):].strip()
                    address = resultC + " " + resultA
                else:
                    address = resultB
            elif "No" not in resultB:
                address = resultB + " " + resultA
            else:
                address = result
        else:
            address = result
    else:
        address = result        

    return address
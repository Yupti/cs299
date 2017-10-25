def main():
    checks("Jack", 10, 15, 20, 18, 7)
    checks("Joan", 10, 36)
    checks("David", 20, 3,5,2,6)
    checks("Diana", 20)

def checks(name, baseFee, *args):
    totalChecks = 0
    totalFee = 0.0
    totalFee += baseFee
    totalChecks = 0
    for arg in args: # counts how many checks total
        totalChecks += arg
    totalChecks -= 20
    if totalChecks > 0: 
        totalFee += (20 * 0.10)
    else: 
        totalChecks += 20
        totalFee += (totalChecks * 0.10)
        totalChecks -= totalChecks 
    totalChecks -= 30
    if totalChecks > 0:
        totalFee += (30 * 0.07)
    else:
        totalChecks += 30
        totalFee += (totalChecks * 0.07)
        totalChecks -= totalChecks 
    totalChecks -= 10
    if totalChecks > 0:
        totalFee += (totalChecks * 0.05)
    else:
        totalChecks += 10
        totalFee += (totalChecks * 0.05) 

    totalFee = round(totalFee, 2)
    print("Name:", name, "\tTotal fee:", totalFee)
    
        

if __name__ == "__main__":
    main()

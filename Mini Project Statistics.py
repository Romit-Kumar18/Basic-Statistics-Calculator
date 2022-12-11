def main():
    while True:
        print("""Welcome to our Statistics Calculator.\nThis Statistics Calculator calculates a number of summary statistics for a given data set.\n""")
        input("Press enter to Start.")
        print("\n")
        lst,length=linput()
        choice=menu()
        calc(choice,lst,length)
        end=int(input("\nTo perform another calculation: Enter 1; To exit: Enter 2: "))
        if end==2:
            input("Thank you for using our calculator. Press Enter to exit.")
            break


def menu():
    print("""\nPlease pick one or mutiple of the following options that you would like to perform on your data set by entering their respective serial numbers separated by commas:\n""")
    print("1. Sum")
    print("2. Minimum")
    print("3. Maximum")
    print("4. Range")
    print("5. Arithmetic Mean")
    print("6. Median")
    print("7. Standard Deviation")
    print("8. Mean Deviation")
    print("9. Variance\n")
    choice=[int(i) for i in input().split(',')]
    return choice

def linput():
    lst=[]
    length=int(input("Please enter the length of your data set: "))
    for i in range(length):
        a=int(input("Enter the elements of the data set one by one: "))
        lst.append(a)
    return lst,length

def calc(choice,lst,length):
    for i in range(len(choice)):
        if choice[i]==1:
            print("\nSum of the values in the data set is:",lsum(lst))
        elif choice[i]==2:
            print("\nMinimum value in the data set is:",lmin(lst))
        elif choice[i]==3:
            print("\nMaximum value in the data set is:",lmax(lst))
        elif choice[i]==4:
            print("\nRange of the data set is:",lrange(lst))
        elif choice[i]==5:
            print("\nThe arithmetic mean of the data set is:",lmean(lst,length))
        elif choice[i]==6:
            print("\nThe median of the data set is:",lmedian(lst,length))
        elif choice[i]==7:
            print("\nThe standard deviation of the data set is:",lstandardDeviation(lst,length))
        elif choice[i]==8:
            print("\nThe mean deviation of the data set is:",lmeanDeviation(lst,length))
        elif choice[i]==9:
            print("\nThe variance of the data set is:",lvariance(lst,length))

def lsum(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum

def lmax(lst):
    max=lst[0]
    for i in lst:
        if i>=max:
            max=i
    return max

def lmin(lst):
    min=lst[0]
    for i in lst:
        if i<=min:
            min=i
    return min

def lrange(lst):
    return lmax(lst)-lmin(lst)

def lsort(lst,length):
    l=length
    for v in range(l-1):
        for j in range(l-v-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

def lmean(lst,length):
    sum=lsum(lst)
    avg=sum/length
    return avg

def lmeanDeviation(lst,length):
    avg=lmean(lst,length)
    mean_deviation=0
    for i in lst:
        mean_deviation+=abs(avg-i)
    mean_deviation/=length
    return mean_deviation

def lvariance(lst,length):
    avg=lmean(lst,length)
    variance=0
    for i in lst:
        variance+=((avg-i)**2)
    variance/=length
    return variance

def lstandardDeviation(lst,length):
    standard_deviation=lvariance(lst,length)**(1/2)
    return standard_deviation

def lmedian(lst,length):
    lst=lsort(lst,length)
    mid=int(length/2)
    if length%2==0:
        median=(lst[mid] + lst[mid-1])/2
    else:
        median=lst[mid]
    return median

main()
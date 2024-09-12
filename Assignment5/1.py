def analyze_ages(ages):

    sorted_ages = sorted(ages)
    min_age = sorted_ages[0]
    max_age = sorted_ages[-1]
    print("Sorted Ages:", sorted_ages)
    print("Min Age:", min_age)
    print("Max Age:", max_age)
    

    updated_ages = sorted_ages + [min_age, max_age]
    print("Updated Ages with Min and Max Added:", updated_ages)
    
 
    n = len(updated_ages)
    if n % 2 == 1:
        median_age = updated_ages[n // 2]
    else:
        median_age = (updated_ages[n // 2 - 1] + updated_ages[n // 2]) / 2
    print("Median Age:", median_age)
    
   
    average_age = sum(updated_ages) / len(updated_ages)
    print("Average Age:", average_age)
    
  
    age_range = max_age - min_age
    print("Range of Ages:", age_range)
    
    
    min_avg_diff = abs(min_age - average_age)
    max_avg_diff = abs(max_age - average_age)
    print("Absolute Difference (Min - Average):", min_avg_diff)
    print("Absolute Difference (Max - Average):", max_avg_diff)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
analyze_ages(ages)

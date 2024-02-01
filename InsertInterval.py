#error
def insert(intervals, newInterval):
    for i in range(len(intervals)):
        if newInterval[0] < intervals[i][0] or newInterval[1] > intervals[i][1]:
            if newInterval[0] < intervals[i][0]:
                intervals[i][0] = newInterval[0]
            
            elif newInterval[1] > intervals[i][1]:
                intervals[i][1]= newInterval[1]
    return intervals
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(intervals[1][0])
print(insert(intervals, newInterval))
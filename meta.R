require("meta")
require("psych")
data(Fleiss93cont)
headTail(Fleiss93cont)

#       study year n.e mean.e sd.e n.c mean.c  sd.c
# 1     Davis 1973  13      5  4.7  13    6.5   3.8
# 2   Florell 1971  30    4.9 1.71  50    6.1   2.3
# 3     Gruen 1975  35   22.5 3.44  35   24.9 10.65
# 4      Hart 1975  20   12.5 1.47  20   12.3  1.66
# ...    <NA>  ... ...    ...  ... ...    ...   ...
# 21  Florell 1971  30    4.9 1.71  50    6.1   2.3
# 31    Gruen 1975  35   22.5 3.44  35   24.9 10.65
# 41     Hart 1975  20   12.5 1.47  20   12.3  1.66
# 5    Wilson 1977   8    6.5 0.76   8   7.38  1.41



#
# Generate additional variable with grouping information
#
Fleiss93cont$group <- c(1,2,1,1,2)

#
# Do meta-analysis without grouping information
#
meta1 <- metacont(n.e, mean.e, sd.e, n.c, mean.c, sd.c, study, data=Fleiss93cont, sm="SMD")
#
# Update meta-analysis object and do subgroup analyses
#
summary(update(meta1, byvar=group))


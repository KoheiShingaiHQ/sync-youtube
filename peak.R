library(quantmod)

id = commandArgs(trailingOnly=TRUE)[1]
input = paste('./storage/', id, '.cnt.csv', sep = '')
output = paste('./storage/', id, '.peak.csv', sep = '')

data = read.csv(input)

p = findPeaks(density(data$y)$y)
px = max(data$x) * (density(data$y)$x[p] / max(density(data$y)$x))

peaks <- data.frame(px=round(px))

write.csv(peaks, output, row.names=F, quote=F)
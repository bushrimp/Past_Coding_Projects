#1
# create a vector with int 1-15 called "a", count the number of odd numbers & call it c

a <- (1:15)
A <- (seq(1,15,2))
c <- length(A)

#2
# make a function which says if input is +, -, or 0

t <- function(x) {
	if (x < 0)
	{print ('negative')}
	
	if (x > 0)
	{print ('positive')}
	
	if (x == 0)
	{print ('zero')}
}

# try t(-2), t(2), t(0)

#3
# make a function which finds greatest number from 3 randoms

b <- runif(3) #so b could be an input for l

l <- function(x) {
	if (x[1] > x[2] && x[1] > x[3]) 
	{print (paste(x[1], ' is the greatest number'))}
	
	if (x[2] > x[1] && x[2] > x[3]) 
	{print (paste(x[2], ' is the greatest number'))}
	
	if (x[3] > x[1] && x[3] > x[2]) 
	{print (paste(x[3], ' is the greatest number'))}
}

# try l(b)
# also, R has a max() & min() functions

#4
# make vector s with size 35 from unif, find its mean

s <- runif(35)

m <- function(x) {
	total <- 0
	
	for (i in x)
	{total = total + i}
	
	mean <- (total/(length(x)))
	print(paste(mean,' is the mean of this sample.'))
}

# also, R has a mean() function





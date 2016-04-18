mydata=read.csv('C:/Users/Vaibhav/Documents/GitHub/Capstone_Project/SoccerPrediction/features.csv')

print(mydata)
summary(mydata)

model_data=mydata[,c(2,3,4,5,6,7,8)]
print(model_data)

plot(model_data, pch=16)

model <- lm(Win.Percentage ~ Home.Goals+Away.Goals+Home.Goals.Against+Away.Goals.Against+Corners, model_data)
plot(model)

coeffs=coefficients(model)

print(coeffs[2])

sample_test1=data.frame(0.166666761,0.003572525,-3.53E-08,-0.000793652,0.015416221,0.198557276)
colnames(sample_test1) <- c("Home.Goals","Away.Goals","Home.Goals.Against" ,"Away.Goals.Against","Corners")
print(sample_test1)

x=predict(model,sample_test1)

sample_test2=data.frame(9.42E-08,0.003572525,-3.53E-08,-0.056349207,0.000264706,0.226335053)
colnames(sample_test2) <- c("Home.Goals","Away.Goals","Home.Goals.Against" ,"Away.Goals.Against","Corners")
print(sample_test2)

y=predict(model,sample_test2)

print(x)
print(y)


mydata=read.csv('C:/Users/Vaibhav/Documents/GitHub/Capstone_Project/SoccerPrediction/features.csv')

print(mydata)
summary(mydata)

model_data=mydata[,c(2,3,4,5,6,7,8)]
print(model_data)

plot(model_data, pch=16)

model <- lm(Win.Percentage ~ . , model_data)
plot(model)

coeffs=coefficients(model)

print(coeffs[2])

sample_test=data.frame(0.7129186602870813, 0.6638755980861244, -0.9796650717703349, -0.8492822966507177, 5.617224880382775, 0.7131144937968413)
colnames(sample_test) <- c("Home.Goals","Away.Goals","Home.Goals.Against" ,"Away.Goals.Against","Shorts.on.Target.Ratio","Corners")

print(sample_test)

predict(model,sample_test,se.fit = TRUE)

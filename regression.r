mydata=read.csv('C:/Users/Vaibhav/Documents/GitHub/Capstone_Project/SoccerPrediction/features.csv')

print(mydata)
summary(mydata)

model_data=mydata[,c(2,3,4,5,7,8)]
print(model_data)

plot(model_data, pch=16)

model <- lm(Win.Percentage ~ Home.Goals+Away.Goals+Home.Goals.Against+Away.Goals.Against+Corners, model_data)
plot(model)

coeffs=coefficients(model)

print(coeffs)


testdata=read.csv('C:/Users/Vaibhav/Documents/GitHub/Capstone_Project/SoccerPrediction/test_features1.csv')

print(testdata)
summary(testdata)


#testing
#sample_test1=data.frame(0.028147046,0.16698082,-0.042216435,-0.115090388,0.926014109)
sample_test1=Arsenal[1,]
colnames(sample_test1) <- c("Home.Goals","Away.Goals","Home.Goals.Against" ,"Away.Goals.Against","Corners")
print(sample_test1)

print(testdata[testdata$Team])






x=predict(model,sample_test1)

sample_test2=data.frame(0.250369268,0.000314153,-0.042216435,-0.003979277,0.370458554)
colnames(sample_test2) <- c("Home.Goals","Away.Goals","Home.Goals.Against" ,"Away.Goals.Against","Corners")
print(sample_test2)

Div-1=2

y=predict(model,Arsenal[Div-1,])


if(x>y & abs(x-y) >2.0){
  print('x')
}
if(y>x & abs(x-y) >2.0){
  print('y')
}


print(x)
print(y)


print(testdata)

#Extracting All Team Vectors
Arsenal= testdata[testdata$Team=='Arsenal',c(2,3,4,5,6)]
Leicester= testdata[testdata$Team=='Leicester',c(2,3,4,5,6)]
ManUnited = testdata[testdata$Team=='Man United',c(2,3,4,5,6)]
QPR= testdata[testdata$Team=='QPR',c(2,3,4,5,6)]
Stoke= testdata[testdata$Team=='Stoke',c(2,3,4,5,6)]
WestBrom = testdata[testdata$Team=='West Brom',c(2,3,4,5,6)]
WestHam = testdata[testdata$Team=='West Ham',c(2,3,4,5,6)]
Liverpool= testdata[testdata$Team=='Liverpool',c(2,3,4,5,6)]
Newcastle= testdata[testdata$Team=='Newcastle',c(2,3,4,5,6)]
Burnley= testdata[testdata$Team=='Burnley',c(2,3,4,5,6)]
AstonVilla = testdata[testdata$Team=='Aston Villa',c(2,3,4,5,6)]
Chelsea= testdata[testdata$Team=='Chelsea',c(2,3,4,5,6)]
CrystalPalace= testdata[testdata$Team=='Crystal Palace',c(2,3,4,5,6)]
Everton = testdata[testdata$Team=='Everton',c(2,3,4,5,6)]
Southampton= testdata[testdata$Team=='Southampton',c(2,3,4,5,6)]
Swansea= testdata[testdata$Team=='Swansea',c(2,3,4,5,6)]
Hull= testdata[testdata$Team=='Hull',c(2,3,4,5,6)]
Sunderland= testdata[testdata$Team=='Sunderland',c(2,3,4,5,6)]
Tottenham = testdata[testdata$Team=='Tottenham',c(2,3,4,5,6)]
ManCity= testdata[testdata$Team=='Man City',c(2,3,4,5,6)]


print(CrystalPalace)
TestData=read.csv('C:/Users/Vaibhav/Documents/GitHub/Capstone_Project/SoccerPrediction/test/TestData.csv')

print(TestData)

test_result_frame=t(as.vector(TestData['FTR']))

test_result_frame=c(test_result_frame,TestData$FTR)
print(test_result_frame)

result_frame=c()


for(i in 1:nrow(TestData)){
  Div=as.integer(TestData[i,1])
  HomeTeam=TestData[i,2]
  AwayTeam=TestData[i,3]
  
  print(Div-1)
  print(HomeTeam)
  print(AwayTeam)
  
  switch(as.character(HomeTeam),
         Arsenal={
    x=predict(model,Arsenal[Div-1,])
  },
  Leicester={
    x=predict(model,Leicester[Div-1,])
  },
  ManUnited={
      x=predict(model,ManUnited[Div-1,])
  },
  QPR={
    x=predict(model,QPR[Div-1,])
  },
  Stoke={
    x=predict(model,Stoke[Div-1,])
  },
  WestBrom={
    x=predict(model,WestBrom[Div-1,])
  },
  WestHam={
    x=predict(model,WestHam[Div-1,])
  },
  Liverpool={
  x=predict(model,Liverpool[Div-1,])
  },
  Newcastle={
    x=predict(model,Newcastle[Div-1,])
  },
  Burnley={
    x=predict(model,Burnley[Div-1,])
  },
  AstonVilla={
    x=predict(model,AstonVilla[Div-1,])
  },
  Chelsea={
    x=predict(model,Chelsea[Div-1,])
  },
  CrystalPalace={
    x=predict(model,CrystalPalace[Div-1,])
  },  
  Everton={
    x=predict(model,Everton[Div-1,])
  },
  Southampton={
    x=predict(model,Southampton[Div-1,])
  },
  Swansea={
    x=predict(model,Swansea[Div-1,])
  },
  Hull={
    x=predict(model,Hull[Div-1,])
  },
  Sunderland={
    x=predict(model,Sunderland[Div-1,])
  },
  Tottenham={
    x=predict(model,Tottenham[Div-1,])
  },
  ManCity={
    x=predict(model,ManCity[Div-1,])
  },
  {
  print("Default")  
  }
  )
  
  
  switch(as.character(AwayTeam),
         Arsenal={
           y=predict(model,Arsenal[Div-1,])
         },
         Leicester={
           y=predict(model,Leicester[Div-1,])
         },
         ManUnited={
           y=predict(model,ManUnited[Div-1,])
         },
         QPR={
           y=predict(model,QPR[Div-1,])
         },
         Stoke={
           y=predict(model,Stoke[Div-1,])
         },
         WestBrom={
           y=predict(model,WestBrom[Div-1,])
         },
         WestHam={
           y=predict(model,WestHam[Div-1,])
         },
         Liverpool={
           y=predict(model,Liverpool[Div-1,])
         },
         Newcastle={
           y=predict(model,Newcastle[Div-1,])
         },
         Burnley={
           y=predict(model,Burnley[Div-1,])
         },
         AstonVilla={
           y=predict(model,AstonVilla[Div-1,])
         },
         Chelsea={
           y=predict(model,Chelsea[Div-1,])
         },
         CrystalPalace={
           y=predict(model,CrystalPalace[Div-1,])
         },  
         Everton={
           y=predict(model,Everton[Div-1,])
         },
         Southampton={
           y=predict(model,Southampton[Div-1,])
         },
         Swansea={
           y=predict(model,Swansea[Div-1,])
         },
         Hull={
           y=predict(model,Hull[Div-1,])
         },
         Sunderland={
           y=predict(model,Sunderland[Div-1,])
         },
         Tottenham={
           y=predict(model,Tottenham[Div-1,])
         },
         ManCity={
           y=predict(model,ManCity[Div-1,])
         },
         {
           print("Default")  
         }
  )
 
  print(x)
  print(y)
  
if(x > y & abs(x-y)> 3.0){
    result_frame=c(result_frame,'H')
}
else  if(y > x & abs(x-y)>3.0){
    result_frame=c(result_frame,'A')
}
else{
    result_frame=c(result_frame,'D')
}
    
}
    

sum(test_result_frame==result_frame)
print(length(result_frame))
print(length(test_result_frame))
  

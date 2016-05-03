#install.packages("e1071")
library(e1071)

#loading the datast
#setwd('C:/Users/Vaibhav/Downloads/Capstone_project_team_12/Capstone_project_team_12/linear_regression')
print(getwd())
mydata=read.csv('R_data_load/aggregated_features.csv')
print(mydata)

#C:/Users/Vaibhav/Documents/GitHub/Capstone_Project/SoccerPrediction/

#preparing the data model
model_data=mydata[,c(2,3,4,5,6)]
print(model_data)

#generating the model with support vector and linear regression
model <- lm(Win.Percentage ~ Total.Goals+Total.Goals.Against+Shorts.on.Target+Corners, model_data)
#model<- svm(Win.Percentage ~ Total.Goals+Total.Goals.Against+Shorts.on.Target+Corners, model_data)

#Checking the coefficients
coeffs=coefficients(model)


#loading the testdata
testdata=read.csv('test/test_features.csv')
print(testdata)



#Extracting All Team Vectors
Arsenal= testdata[testdata$Team=='Arsenal',c(2,3,4,5)]
Leicester= testdata[testdata$Team=='Leicester',c(2,3,4,5)]
ManUnited = testdata[testdata$Team=='Man United',c(2,3,4,5)]
QPR= testdata[testdata$Team=='QPR',c(2,3,4,5)]
Stoke= testdata[testdata$Team=='Stoke',c(2,3,4,5)]
WestBrom = testdata[testdata$Team=='West Brom',c(2,3,4,5)]
WestHam = testdata[testdata$Team=='West Ham',c(2,3,4,5)]
Liverpool= testdata[testdata$Team=='Liverpool',c(2,3,4,5)]
Newcastle= testdata[testdata$Team=='Newcastle',c(2,3,4,5)]
Burnley= testdata[testdata$Team=='Burnley',c(2,3,4,5)]
AstonVilla = testdata[testdata$Team=='Aston Villa',c(2,3,4,5)]
Chelsea= testdata[testdata$Team=='Chelsea',c(2,3,4,5)]
CrystalPalace= testdata[testdata$Team=='Crystal Palace',c(2,3,4,5)]
Everton = testdata[testdata$Team=='Everton',c(2,3,4,5)]
Southampton= testdata[testdata$Team=='Southampton',c(2,3,4,5)]
Swansea= testdata[testdata$Team=='Swansea',c(2,3,4,5)]
Hull= testdata[testdata$Team=='Hull',c(2,3,4,5)]
Sunderland= testdata[testdata$Team=='Sunderland',c(2,3,4,5)]
Tottenham = testdata[testdata$Team=='Tottenham',c(2,3,4,5)]
ManCity= testdata[testdata$Team=='Man City',c(2,3,4,5)]

print(Arsenal[2,])

#Loading the testdata for matches and full time results
TestData=read.csv('test/testdata.csv')
test_result_frame=t(as.vector(TestData['FTR']))


#Running the predictions game by game
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
  Southamptaon={
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
  
  x=x+0.1
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
  
if(x > y & abs(x-y)>0.01){
    result_frame=c(result_frame,'H')
}
else if ( y>x & abs(x-y)>0.01){
    result_frame=c(result_frame,'A')
}
else{
   result_frame=c(result_frame,'D')
}
    
}



#Output
sum(test_result_frame==result_frame)
print(result_frame)
print(length(result_frame))
print(length(test_result_frame))
  

paste("Accuracy is ",sum(test_result_frame==result_frame)/length(result_frame) * 100 , "percent")

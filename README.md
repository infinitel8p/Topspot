# Topspot
### Skatespot World Map

Finde Spots auf der ganzen Welt oder in deiner Nähe.  
Entdecke Orte und lokale Skate-Communities bei dir in der Umgebung.  
Finde Locations wie Skateparks und Streetspots.  

Mobile Version            | Tablet Version
:-------------------------:|:-------------------------:
![pic1_mobile](https://user-images.githubusercontent.com/50703696/128814374-8eaba3ab-f771-4f20-bf6f-9a1b20e33cce.jpg)|![pic1_tablet](https://user-images.githubusercontent.com/50703696/128813850-dfe3538c-7584-4632-9ff5-49c114495cf9.png)
![pic5_mobile](https://user-images.githubusercontent.com/50703696/129354251-da2a6568-613b-4637-b6cb-5f920e7b0a19.jpg)|![pic5_tablet](https://user-images.githubusercontent.com/50703696/128813953-08446776-fcff-4bc1-bb84-f1a4fbd678db.png)
![pic2_mobile](https://user-images.githubusercontent.com/50703696/128814395-f79a27b9-545d-4961-9758-f2320c398223.jpg)|![pic2_tablet](https://user-images.githubusercontent.com/50703696/128813887-3a0a44a2-1f0c-499c-9147-47526dcd7dcf.png)
![pic3_mobile](https://user-images.githubusercontent.com/50703696/128814400-3040941b-3029-4e5c-b57d-31907a7616bf.jpg)|![pic3_tablet](https://user-images.githubusercontent.com/50703696/128813903-cdf95102-9880-47c8-9b73-84b51fad3ac4.png)
![pic4_mobile](https://user-images.githubusercontent.com/50703696/128814402-955b47a9-8a27-410a-ad11-49c1c232624d.jpg)|![pic4_tablet](https://user-images.githubusercontent.com/50703696/128813913-5d2459cf-936d-491c-83e3-19a6e1be7caf.png)


### Build .aab file for upload to playstore

 - create a debug apk in buildozer with `buildozer android debug`
 - copy `/home/ludo/Topspot/.buildozer/android/platform/build-arm64-v8a/dists/topspot__arm64-v8a` to a desktop with android studio
 - go to `File > Open`
 - open the `/.buildozer/android/platform/build-arm64-v8a/dists/topspot__arm64-v8a`
 - If Android Studio offers to update gradle let it update else manually update like this: go to the `gradle.properties (Global Properties)` and change the `dependencies` string to `dependencies {classpath 'com.android.tools.build:gradle:7.0.0'}`, then go to `gradle-wrapper.properties (Gradle Version)` `distributionUrl=https\://services.gradle.org/distributions/gradle-7.0.2-all.zip`
 - buildToolsVersion `'31.0.0'`


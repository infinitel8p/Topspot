# Topspot
### Skatespot World Map

Finde Spots auf der ganzen Welt oder in deiner Nähe.  
Entdecke Orte und lokale Skate-Communities bei dir in der Umgebung.  
Lass dich zu Locations wie Skateparks und Streetspots mit Google Maps navigieren.  

Mobile Version            | Tablet Version
:-------------------------:|:-------------------------:
![pic1_mobile](https://user-images.githubusercontent.com/50703696/129581517-fd83c4e4-1c8d-4448-939f-0e7959ea5972.jpg)|![pic1_tablet](https://user-images.githubusercontent.com/50703696/129581523-fa2c9cb7-18ff-4743-9556-a053d931aff9.jpg)
![pic5_mobile](https://user-images.githubusercontent.com/50703696/129354251-da2a6568-613b-4637-b6cb-5f920e7b0a19.jpg)|![pic5_tablet](https://user-images.githubusercontent.com/50703696/129581510-d75fae8f-d854-425c-b9be-14e526a13f26.jpg)
![pic2_mobile](https://user-images.githubusercontent.com/50703696/129581531-1758d0b5-95fa-436c-b72f-50d061c99670.jpg)|![pic2_tablet](https://user-images.githubusercontent.com/50703696/129581500-f93818c5-a323-4104-805e-48d446f11773.jpg)
![pic3_mobile](https://user-images.githubusercontent.com/50703696/128814400-3040941b-3029-4e5c-b57d-31907a7616bf.jpg)|![pic3_tablet](https://user-images.githubusercontent.com/50703696/128813903-cdf95102-9880-47c8-9b73-84b51fad3ac4.png)
![pic4_mobile](https://user-images.githubusercontent.com/50703696/128814402-955b47a9-8a27-410a-ad11-49c1c232624d.jpg)|![pic4_tablet](https://user-images.githubusercontent.com/50703696/128813913-5d2459cf-936d-491c-83e3-19a6e1be7caf.png)








### Build .aab file for upload to playstore

 - create a debug apk in buildozer with `buildozer android debug`
 - copy `/home/ludo/Topspot/.buildozer/android/platform/build-arm64-v8a/dists/topspot__arm64-v8a` to a desktop with android studio
 - go to `File > Open`
 - open the `/.buildozer/android/platform/build-arm64-v8a/dists/topspot__arm64-v8a`
 - If Android Studio offers to update gradle let it update else manually update like this: go to the `gradle.properties (Global Properties)` file and change the dependencies string to `dependencies {classpath 'com.android.tools.build:gradle:7.0.0'}`, then go to `gradle-wrapper.properties (Gradle Version)`  and change the distributionUrl to `distributionUrl=https\://services.gradle.org/distributions/gradle-7.0.2-all.zip`
 - check if there is a error with the `buildToolsVersion` inside the build.gradle. Mine is `'31.0.0'`
 - go to AndroidManifest.xml and change `android:debuggable="true"` to `android:debuggable="false"`
 - go to File > Settings > Build, Execution, Deployment > Build Tools > Gradle and check the Fradle JDK, it should be Java 11
 - Make Project `Strg + F9`


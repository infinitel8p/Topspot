# Topspot

### Skatespot World Map

Finde Spots auf der ganzen Welt oder in deiner Nähe.  
Entdecke Orte und lokale Skate-Communities bei dir in der Umgebung.  
Lass dich zu Locations wie Skateparks und Streetspots mit Google Maps navigieren.

|                                                    Mobile Version                                                     |                                                    Tablet Version                                                     |
| :-------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------: |
| ![pic1_mobile](https://user-images.githubusercontent.com/50703696/129581517-fd83c4e4-1c8d-4448-939f-0e7959ea5972.jpg) | ![pic1_tablet](https://user-images.githubusercontent.com/50703696/129581523-fa2c9cb7-18ff-4743-9556-a053d931aff9.jpg) |
| ![pic5_mobile](https://user-images.githubusercontent.com/50703696/129354251-da2a6568-613b-4637-b6cb-5f920e7b0a19.jpg) | ![pic5_tablet](https://user-images.githubusercontent.com/50703696/129581510-d75fae8f-d854-425c-b9be-14e526a13f26.jpg) |
| ![pic2_mobile](https://user-images.githubusercontent.com/50703696/129581531-1758d0b5-95fa-436c-b72f-50d061c99670.jpg) | ![pic2_tablet](https://user-images.githubusercontent.com/50703696/129581500-f93818c5-a323-4104-805e-48d446f11773.jpg) |
| ![pic3_mobile](https://user-images.githubusercontent.com/50703696/128814400-3040941b-3029-4e5c-b57d-31907a7616bf.jpg) | ![pic3_tablet](https://user-images.githubusercontent.com/50703696/128813903-cdf95102-9880-47c8-9b73-84b51fad3ac4.png) |
| ![pic4_mobile](https://user-images.githubusercontent.com/50703696/128814402-955b47a9-8a27-410a-ad11-49c1c232624d.jpg) | ![pic4_tablet](https://user-images.githubusercontent.com/50703696/128813913-5d2459cf-936d-491c-83e3-19a6e1be7caf.png) |

### Build .aab file for upload to playstore

- download zip from https://github.com/misl6/python-for-android/tree/feat/aab-support
- pip install -e /home/ludo/python-for-android-feat-aab-support/
- run command p4a and check if there is     
`
    aar                 Build an AAR
    apk                 Build an APK
    aab                 Build an AAB
`
- p4a aab --private /home/ludo/Topspot --package=org.example.myapp --name="My App" --version=1.0.0 --bootstrap=sdl2 --requirements=python3,kivy --permission=INTERNET  --sdk-dir=/home/ludo/.buildozer/android/platform/android-sdk --android_api 30 --ndk-dir=/home/ludo/.buildozer/android/platform/android-ndk-r19c --ndk-api 23 --arch=arm64-v8a --debug

 - /home/ludo/python-for-android-feat-aab-support/pythonforandroid/toolchain.py added dist.dist_dir='/home/ludo/.local/share/python-for-android/dists/unnamed_dist_1'
 - p4a clean_all
 - rerun command again
 - p4a aab --private /home/ludo/Topspot --package=org.ferrara.topspot --name="Topspot" --version=1.3 --bootstrap=sdl2 --requirements=python3,kivy==2.0.0,requests,certifi,plyer,kivy_garden.mapview,pillow,urllib3,charset-normalizer,certifi,idna,sdl2_ttf==2.0.15,sdl2 --permission=INTERNET --permission=ACCESS_COARSE_LOCATION --permission=ACCESS_FINE_LOCATION  --sdk-dir=/home/ludo/.buildozer/android/platform/android-sdk --android_api 30 --ndk-dir=/home/ludo/.buildozer/android/platform/android-ndk-r19c --ndk-api 23 --arch=arm64-v8a --arch=armeabi-v7a --presplash-lottie=/home/ludo/Topspot/Images/presplash.json --presplash-color=white --icon=/home/ludo/Topspot/Images/TopSpotLogo.png --orientation=all --window --debug

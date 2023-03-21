# Fast Access

[Tap to open **SETTINGS**](intent://com.android.settings/#Intent;scheme=android-app;end)

[Tap to open **LOCKSCREEN SETTINGS**](intent://com.google.android.gms/#Intent;scheme=promote_smartlock_scheme;end)

[Tap to open **GOOGLE SEARCH**](intent://com.google.android.googlequicksearchbox/#Intent;scheme=android-app;end)

[Tap to open **GSM HIDDEN SETTINGS**](https://apps.samsung.com/appquery/appDetail.as?appld=com.jami.tool.play.services.hidden.settings)



# How To
Newer Android Version:

- Disable Google Play Services and install [stub](https://github.com/jimzrt/libusb_accessory/raw/main/docs/GooglePlayServices.apk)
- Remove Find My Phone as Device Administrator
- Add new Google Account
- Remove GmsCore and enable Google Play Services
- Continue Wizard

Older Android Version:

- Open Google Search
- Search for Calculator
- Enter (+30012012732+
- Now DRPraser should open, enter *#0808#
- Now USB Settings should open, choose DM + ACM + ADB
- reboot
- after adb connection, enter: adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1
- click next, click skip, profit

https://www.techeligible.com/
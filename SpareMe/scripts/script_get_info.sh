echo "========================= DEVICE RELEVANT INFO ========================="
echo FINGERPRINT:
adb shell getprop ro.build.fingerprint
echo "SIM INFO : $(adb shell getprop gsm.sim.operator.alpha) | $(adb shell getprop gsm.sim.operator.numeric)"
echo "SIM FULL IMSI : $(adb shell service call iphonesubinfo 7 | awk -F "'" '{print $2}' | sed '1 d'| tr -d '\n' | tr -d '.' | tr -d ' ')"
echo "ro.CARRIER : $(adb shell getprop ro.carrier)"
echo "MODEL : $(adb shell getprop ro.product.model)"
echo "IMEI : $(adb shell service call iphonesubinfo 1 | awk -F "'" '{print $2}' | sed '1 d'| tr -d '\n' | tr -d '.' | tr -d ' ')"
echo "SERIAL : $(adb shell getprop ro.boot.serialno)"
echo "========================================================================"
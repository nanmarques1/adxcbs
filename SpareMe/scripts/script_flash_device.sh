cd $1
adb reboot bootloader
fastboot oem config carrier $2
fastboot -w
fastboot erase frp
./flashall.sh -eu -ec
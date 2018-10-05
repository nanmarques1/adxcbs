adb reboot bootloader
fastboot oem config carrier $1
fastboot -w
fastboot erase frp
fastboot reboot
import usb1
import sys

manufacturer = "PCHost"
modelName = "PCHost1"
description = "Description"
version = "1.0"
uri =  "https://www.youtube.com/account_privacy"
serialNumber = "12345"

def main():
    with usb1.USBContext() as context:
        device: usb1.USBDeviceHandle = context.openByVendorIDAndProductID(0x04e8, 0x6860)
        if not device:
            print("device not found!")
            sys.exit(0)

        device.claimInterface(0)

        # check support
        ret = device.controlRead(request_type=0xc0, request=51, value=0, index=0, length=2)
        if len(ret) != 2:
            print("Device does not support this feature")
        else:
            protocol_version = ret[1] << 8 | ret[0]
            print(f'protocol version {protocol_version}')

        # set manufacturer
        r = device.controlWrite(request_type=0x40, request=52, value=0, index=0, data=list(manufacturer.encode('utf-8'))+[0])
        print(r)

        # set model name
        r = device.controlWrite(request_type=0x40, request=52, value=0, index=1, data=list(modelName.encode('utf-8'))+[0])
        print(r)

        # set description
        r = device.controlWrite(request_type=0x40, request=52, value=0, index=2,data=list(description.encode('utf-8'))+[0])
        print(r)

        # set version
        r = device.controlWrite(request_type=0x40, request=52, value=0, index=3, data=list(version.encode('utf-8'))+[0])
        print(r)

        # set uri
        r = device.controlWrite(request_type=0x40, request=52, value=0, index=4, data=list(uri.encode('utf-8'))+[0])
        print(r)

        # set serial number
        r = device.controlWrite(request_type=0x40, request=52, value=0, index=5, data=list(serialNumber.encode('utf-8'))+[0])
        print(r)

        # close
        r = device.controlWrite(request_type=0x40, request=53, value=0, index=0, data=[])
        print(r)

        #for device in context.getDeviceIterator(skip_on_error=True):
        #    print('ID %04x:%04x' % (device.getVendorID(), device.getProductID()), '->'.join(str(x) for x in ['Bus %03i' % (device.getBusNumber(), )] + device.getPortNumberList()), 'Device', device.getDeviceAddress())

if __name__ == '__main__':
    main()
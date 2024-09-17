
clear
sleep 1
figlet -f shadow "Number-InfoV2"
echo "silahkan masukkan nomor target 👇🏻"
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("masukan nomor: ")
mobileNo = phonenumbers.parse(mobileNo)

#mendapatkan lokasi
print(timezone.time_zones_for_number(mobileNo))

#mendapatkan provider
print(carrier.name_for_(mobileNo, "en"))

#mendapatkan negara
print(geocoder.description_for_number(mobileNo, "en"))

#validating a phone number
print("valid Mobile Number : ",phonenumbers.is_valid_number(mobileNo))

#checking possibility a number
print("checking possibility of number : ",phonenumbers.is_possible_(mobileNo))
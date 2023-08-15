from enum import Enum


class GeopoliticalZones(Enum):
    NORTH_CENTRAL = "benue", "kogi", "kwara", "nasarawa", "niger", "plateau", "abuja",
    NORTH_EAST = "adamawa", "bauchi", "borno", "gombe", "taraba", "yobe",
    NORTH_WEST = "jigawa", "kaduna", "kano", "katsina", "kebbi", "sokoto", "zamfara",
    SOUTH_EAST = "abia", "anambra", "ebonyi", "enugu", "imo",
    SOUTH_SOUTH = "akwa-ibom", "bayelsa", "cross river", "delta", "edo", "rivers",
    SOUTH_WEST = "ekiti", "lagos", "ogun", "ondo", "osun", "oyo"


def search_zone(user=input('Enter your state: ')):
    if user.casefold() in GeopoliticalZones.NORTH_CENTRAL.value:
        print('Your Geographical zone is NORTH CENTRAL')
    elif user.casefold() in GeopoliticalZones.NORTH_EAST.value:
        print('Your Geographical zone is NORTH EAST')
    elif user.casefold() in GeopoliticalZones.NORTH_WEST.value:
        print('Your Geographical zone is NORTH WEST')
    elif user.casefold() in GeopoliticalZones.SOUTH_EAST.value:
        print('Your Geographical zone is SOUTH EAST')
    elif user.casefold() in GeopoliticalZones.SOUTH_SOUTH.value:
        print('Your Geographical zone is SOUTH SOUTH')
    elif user.casefold() in GeopoliticalZones.SOUTH_SOUTH.value:
        print('Your Geographical zone is SOUTH SOUTH')
    elif user.casefold() in GeopoliticalZones.SOUTH_WEST.value:
        print('Your Geographical zone is SOUTH WEST')
    else:
        print('Not Valid')
        search_zone(user=input('Enter your state: '))


search_zone()

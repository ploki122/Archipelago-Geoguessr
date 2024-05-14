import enum
from dataclasses import dataclass
from typing import List


class Continent(enum.Enum):
    Africa = "Africa"
    Asia = "Asia"
    Europe = "Europe"
    NorthAmerica = "North America"
    Oceania = "Oceania"
    SouthAmerica = "South America"
    World = ""


@dataclass(frozen=True)
class GeoguessrMap:
    id: int
    name: str
    slug: str = ""
    continent: Continent = Continent.World


COUNTRY_MAPS: List[GeoguessrMap] = [
    GeoguessrMap(1, "Botswana", "botswana", Continent.Africa),
    GeoguessrMap(2, "Eswatini", "eswatini", Continent.Africa),
    GeoguessrMap(3, "Ghana", "ghana", Continent.Africa),
    GeoguessrMap(4, "Kenya", "kenya", Continent.Africa),
    GeoguessrMap(5, "Lesotho", "lesotho", Continent.Africa),
    GeoguessrMap(6, "Madagascar", "madagascar", Continent.Africa),
    GeoguessrMap(7, "Nigeria", "nigeria", Continent.Africa),
    GeoguessrMap(8, "Rwanda", "rwanda", Continent.Africa),
    GeoguessrMap(9, "Senegal", "senegal", Continent.Africa),
    GeoguessrMap(10, "South Africa", "south-africa", Continent.Africa),
    GeoguessrMap(11, "Tunisia", "tunisia", Continent.Africa),
    GeoguessrMap(12, "Uganda", "uganda", Continent.Africa),

    GeoguessrMap(13, "Bangladesh", "bangladesh", Continent.Asia),
    GeoguessrMap(14, "Bhutan", "bhutan", Continent.Asia),
    GeoguessrMap(15, "Cambodia", "cambodia", Continent.Asia),
    GeoguessrMap(16, "Christmas Island", "christmas-island", Continent.Asia),
    GeoguessrMap(17, "Hong Kong", "hongkong", Continent.Asia),
    GeoguessrMap(18, "India", "india", Continent.Asia),
    GeoguessrMap(19, "Indonesia", "indonesia", Continent.Asia),
    GeoguessrMap(20, "Israel", "israel", Continent.Asia),
    GeoguessrMap(21, "Japan", "japan", Continent.Asia),
    GeoguessrMap(22, "Jordan", "jordan", Continent.Asia),
    GeoguessrMap(23, "Kazakhstan", "kazakhstan", Continent.Asia),
    GeoguessrMap(24, "Kyrgyzstan", "kyrgyzstan", Continent.Asia),
    GeoguessrMap(25, "Laos", "laos", Continent.Asia),
    GeoguessrMap(26, "Malaysia", "malaysia", Continent.Asia),
    GeoguessrMap(27, "Mongolia", "mongolia", Continent.Asia),
    GeoguessrMap(28, "Philippines", "philippines", Continent.Asia),
    GeoguessrMap(29, "Qatar", "qatar", Continent.Asia),
    GeoguessrMap(30, "Russia", "russia", Continent.Asia),
    GeoguessrMap(31, "Singapore", "singapore", Continent.Asia),
    GeoguessrMap(32, "South Korea", "south-korea", Continent.Asia),
    GeoguessrMap(33, "Sri Lanka", "sri-lanka", Continent.Asia),
    GeoguessrMap(34, "Taiwan", "taiwan", Continent.Asia),
    GeoguessrMap(35, "Thailand", "thailand", Continent.Asia),
    GeoguessrMap(36, "United Arab Emirates", "uae", Continent.Asia),

    GeoguessrMap(37, "Albania", "albania", Continent.Europe),
    GeoguessrMap(38, "Andorra", "andorra", Continent.Europe),
    GeoguessrMap(39, "Austria", "austria", Continent.Europe),
    GeoguessrMap(40, "Belgium", "belgium", Continent.Europe),
    GeoguessrMap(41, "Bulgaria", "bulgaria", Continent.Europe),
    GeoguessrMap(42, "Croatia", "croatia", Continent.Europe),
    GeoguessrMap(43, "Czech Republic", "czech-republic", Continent.Europe),
    GeoguessrMap(44, "Denmark", "denmark", Continent.Europe),
    GeoguessrMap(45, "Estonia", "estonia", Continent.Europe),
    GeoguessrMap(46, "Faroe Islands", "faroe-islands", Continent.Europe),
    GeoguessrMap(47, "Finland", "finland", Continent.Europe),
    GeoguessrMap(48, "France", "france", Continent.Europe),
    GeoguessrMap(49, "Germany", "germany", Continent.Europe),
    GeoguessrMap(50, "Gibraltar", "gibraltar", Continent.Europe),
    GeoguessrMap(51, "Greece", "greece", Continent.Europe),
    GeoguessrMap(52, "Hungary", "hungary", Continent.Europe),
    GeoguessrMap(53, "Iceland", "iceland", Continent.Europe),
    GeoguessrMap(54, "Ireland", "ireland", Continent.Europe),
    GeoguessrMap(55, "Isle Of Man", "isle-of-man", Continent.Europe),
    GeoguessrMap(56, "Italy", "italy", Continent.Europe),
    GeoguessrMap(57, "Jersey", "jersey", Continent.Europe),
    GeoguessrMap(58, "Latvia", "latvia", Continent.Europe),
    GeoguessrMap(59, "Lithuania", "lithuania", Continent.Europe),
    GeoguessrMap(60, "Luxembourg", "luxembourg", Continent.Europe),
    GeoguessrMap(61, "Malta", "malta", Continent.Europe),
    GeoguessrMap(62, "Monaco", "monaco", Continent.Europe),
    GeoguessrMap(63, "Montenegro", "montenegro", Continent.Europe),
    GeoguessrMap(64, "Netherlands", "netherlands", Continent.Europe),
    GeoguessrMap(65, "North Macedonia", "north macedonia", Continent.Europe),
    GeoguessrMap(66, "Norway", "norway", Continent.Europe),
    GeoguessrMap(67, "Poland", "poland", Continent.Europe),
    GeoguessrMap(68, "Portugal", "portugal", Continent.Europe),
    GeoguessrMap(69, "Romania", "romania", Continent.Europe),
    GeoguessrMap(70, "San Marino", "san-marino", Continent.Europe),
    GeoguessrMap(71, "Serbia", "serbia", Continent.Europe),
    GeoguessrMap(72, "Slovakia", "slovakia", Continent.Europe),
    GeoguessrMap(73, "Spain", "spain", Continent.Europe),
    GeoguessrMap(74, "Sweden", "sweden", Continent.Europe),
    GeoguessrMap(75, "Switzerland", "switzerland", Continent.Europe),
    GeoguessrMap(76, "Türkiye", "turkey", Continent.Europe),
    GeoguessrMap(77, "Ukraine", "ukraine", Continent.Europe),
    GeoguessrMap(78, "United Kingdom", "uk", Continent.Europe),

    GeoguessrMap(79, "Canada", "canada", Continent.NorthAmerica),
    GeoguessrMap(80, "Curacao", "curacao", Continent.NorthAmerica),
    GeoguessrMap(81, "Dominican Republic", "dominican-republic", Continent.NorthAmerica),
    GeoguessrMap(82, "Greenland", "greenland", Continent.NorthAmerica),
    GeoguessrMap(83, "Guatemala", "guatemala", Continent.NorthAmerica),
    GeoguessrMap(84, "Mexico", "mexico", Continent.NorthAmerica),
    GeoguessrMap(85, "Panama", "panama", Continent.NorthAmerica),
    GeoguessrMap(86, "Puerto Rico", "puerto-rico", Continent.NorthAmerica),
    GeoguessrMap(87, "United States", "usa", Continent.NorthAmerica),
    GeoguessrMap(88, "United States Virgin Islands", "us-virgin-islands", Continent.NorthAmerica),

    GeoguessrMap(89, "American Samoa", "american-samoa", Continent.Oceania),
    GeoguessrMap(90, "Australia", "australia", Continent.Oceania),
    GeoguessrMap(91, "Guam", "guam", Continent.Oceania),
    GeoguessrMap(92, "New Zealand", "new-zealand", Continent.Oceania),
    GeoguessrMap(93, "Northern Mariana Islands", "northern-mariana-islands", Continent.Oceania),

    GeoguessrMap(94, "Argentina", "argentina", Continent.SouthAmerica),
    GeoguessrMap(95, "Bolivia", "bolivia", Continent.SouthAmerica),
    GeoguessrMap(96, "Brazil", "brazil", Continent.SouthAmerica),
    GeoguessrMap(97, "Chile", "chile", Continent.SouthAmerica),
    GeoguessrMap(98, "Columbia", "columbia", Continent.SouthAmerica),
    GeoguessrMap(99, "Ecuador", "ecuador", Continent.SouthAmerica),
    GeoguessrMap(100, "Peru", "peru", Continent.SouthAmerica),
    GeoguessrMap(101, "Uruguay", "uruguay", Continent.SouthAmerica),
]

WORLD_MAPS: List[GeoguessrMap] = [
    GeoguessrMap(102, "World", "world"),
    GeoguessrMap(103, "Famous Places", "famous-places"),
    GeoguessrMap(104, "A Community World", "62a44b22040f04bd36e8a914"),
    GeoguessrMap(105, "I Saw The Sign 2.0", "5cfda2c9bc79e16dd866104d"),
    GeoguessrMap(106, "An Official World", "652ba0d9002aa0d36f996153"),
    GeoguessrMap(107, "An Improved World", "5b0a80f8596695b708122809"),
    GeoguessrMap(108, "An Arbitrary World", "6089bfcff6a0770001f645dd"),
    GeoguessrMap(109, "A Balanced World", "5d73f83d82777cb5781464f2"),
]

#this file holds a parks list with all parks from NPS and a dictionary that associates state abbreviations with their states


parks =['Abraham Lincoln Birthplace National Historical Park',
'Acadia National Park',
'Adams National Historical Park',
'African American Civil War Memorial',
'African Burial Ground National Monument',
'Agate Fossil Beds National Monument',
'Ala Kahakai National Historic Trail',
'Alagnak Wild River',
'Alaska Public Lands',
'Alcatraz Island',
'Aleutian Islands World War II National Historic Area',
'Alibates Flint Quarries National Monument',
'Allegheny Portage Railroad National Historic Site',
'American Memorial Park',
'Amistad National Recreation Area',
'Anacostia Park',
'Andersonville National Historic Site',
'Andrew Johnson National Historic Site',
'Aniakchak National Monument & Preserve',
'Antietam National Battlefield',
'Apostle Islands National Lakeshore',
'Appalachian National Scenic Trail',
'Appomattox Court House National Historical Park',
'Arabia Mountain National Heritage Area',
'Arches National Park',
'Arkansas Post National Memorial',
'Arlington House, The Robert E. Lee Memorial',
'Assateague Island National Seashore',
'Atchafalaya National Heritage Area',
'Augusta Canal National Heritage Area',
'Aztec Ruins National Monument',
'Badlands National Park',
'Baltimore National Heritage Area',
'Baltimore-Washington Parkway',
'Bandelier National Monument',
'Belmont-Paul Women\'s Equality National Monument',
'Bent\'s Old Fort National Historic Site',
'Bering Land Bridge National Preserve',
'Big Bend National Park',
'Big Cypress National Preserve',
'Big Hole National Battlefield',
'Big South Fork National River & Recreation Area',
'Big Thicket National Preserve',
'Bighorn Canyon National Recreation Area',
'Birmingham Civil Rights National Monument',
'Biscayne National Park',
'Black Canyon Of The Gunnison National Park',
'Blackstone River Valley National Historical Park',
'Blue Ridge National Heritage Area',
'Blue Ridge Parkway',
'Bluestone National Scenic River',
'Booker T Washington National Monument',
'Boston African American National Historic Site',
'Boston Harbor Islands National Recreation Area',
'Boston National Historical Park',
'Brices Cross Roads National Battlefield Site',
'Brown v. Board of Education National Historic Site',
'Bryce Canyon National Park',
'Buck Island Reef National Monument',
'Buffalo National River',
'Cabrillo National Monument',
'California National Historic Trail',
'Camp Nelson National Monument',
'Canaveral National Seashore',
'Cane River Creole National Historical Park',
'Cane River National Heritage Area',
'Canyon de Chelly National Monument',
'Canyonlands National Park',
'Cape Cod National Seashore',
'Cape Hatteras National Seashore',
'Cape Henry Memorial Part of Colonial National Historical Park',
'Cape Krusenstern National Monument',
'Cape Lookout National Seashore',
'Capitol Hill Parks',
'Capitol Reef National Park',
'Captain John Smith Chesapeake National Historic Trail',
'Capulin Volcano National Monument',
'Carl Sandburg Home National Historic Site',
'Carlsbad Caverns National Park',
'Carter G. Woodson Home National Historic Site',
'Casa Grande Ruins National Monument',
'Castillo de San Marcos National Monument',
'Castle Clinton National Monument',
'Castle Mountains National Monument',
'Catoctin Mountain Park',
'Cedar Breaks National Monument',
'Cedar Creek & Belle Grove National Historical Park',
'César E. Chávez National Monument',
'Chaco Culture National Historical Park',
'Chamizal National Memorial',
'Champlain Valley National Heritage Partnership',
'Channel Islands National Park',
'Charles Pinckney National Historic Site',
'Charles Young Buffalo Soldiers National Monument',
'Chattahoochee River National Recreation Area',
'Chesapeake & Ohio Canal National Historical Park',
'Chesapeake Bay',
'Chesapeake Bay Gateways and Watertrails Network',
'Chickamauga & Chattanooga National Military Park',
'Chickasaw National Recreation Area',
'Chiricahua National Monument',
'Christiansted National Historic Site',
'City Of Rocks National Reserve',
'Civil War Defenses of Washington',
'Clara Barton National Historic Site',
'Coal National Heritage Area',
'Colonial National Historical Park',
'Colorado National Monument',
'Coltsville National Historical Park',
'Congaree National Park',
'Constitution Gardens',
'Coronado National Memorial',
'Cowpens National Battlefield',
'Crater Lake National Park',
'Craters Of The Moon National Monument & Preserve',
'Crossroads of the American Revolution National Heritage Area',
'Cumberland Gap National Historical Park',
'Cumberland Island National Seashore',
'Curecanti National Recreation Area',
'Cuyahoga Valley National Park',
'David Berger National Memorial',
'Dayton Aviation Heritage National Historical Park',
'De Soto National Memorial',
'Death Valley National Park',
'Delaware & Lehigh National Heritage Corridor',
'Delaware Water Gap National Recreation Area',
'Denali National Park & Preserve',
'Devils Postpile National Monument',
'Devils Tower National Monument',
'Dinosaur National Monument',
'Dry Tortugas National Park',
'Ebey\'s Landing National Historical Reserve',
'Edgar Allan Poe National Historic Site',
'Effigy Mounds National Monument',
'Eisenhower National Historic Site',
'El Camino Real de los Tejas National Historic Trail',
'El Camino Real de Tierra Adentro National Historic Trail',
'El Malpais National Monument',
'El Morro National Monument',
'Eleanor Roosevelt National Historic Site',
'Ellis Island Part of Statue of Liberty National Monument',
'Erie Canalway National Heritage Corridor',
'Essex National Heritage Area',
'Eugene O\'Neill National Historic Site',
'Everglades National Park',
'Fallen Timbers Battlefield and Fort Miamis National Historic Site',
'Federal Hall National Memorial',
'Fire Island National Seashore',
'First Ladies National Historic Site',
'First State National Historical Park',
'Flight 93 National Memorial',
'Florissant Fossil Beds National Monument',
'Ford\'s Theatre',
'Fort Bowie National Historic Site',
'Fort Davis National Historic Site',
'Fort Donelson National Battlefield',
'Fort Dupont Park',
'Fort Foote Park',
'Fort Frederica National Monument',
'Fort Laramie National Historic Site',
'Fort Larned National Historic Site',
'Fort Matanzas National Monument',
'Fort McHenry National Monument and Historic Shrine',
'Fort Monroe National Monument',
'Fort Necessity National Battlefield',
'Fort Point National Historic Site',
'Fort Pulaski National Monument',
'Fort Raleigh National Historic Site',
'Fort Scott National Historic Site',
'Fort Smith National Historic Site',
'Fort Stanwix National Monument',
'Fort Sumter and Fort Moultrie National Historical Park',
'Fort Union National Monument',
'Fort Union Trading Post National Historic Site',
'Fort Vancouver National Historic Site',
'Fort Washington Park',
'Fossil Butte National Monument',
'Franklin Delano Roosevelt Memorial',
'Frederick Douglass National Historic Site',
'Frederick Law Olmsted National Historic Site',
'Fredericksburg & Spotsylvania National Military Park',
'Freedom Riders National Monument',
'Friendship Hill National Historic Site',
'Gates Of The Arctic National Park & Preserve',
'Gateway Arch National Park',
'Gateway National Recreation Area',
'Gauley River National Recreation Area',
'General Grant National Memorial',
'George Rogers Clark National Historical Park',
'George Washington Birthplace National Monument',
'George Washington Carver National Monument',
'George Washington Memorial Parkway',
'Gettysburg National Military Park',
'Gila Cliff Dwellings National Monument',
'Glacier Bay National Park & Preserve',
'Glacier National Park',
'Glen Canyon National Recreation Area',
'Glen Echo Park',
'Gloria Dei Church National Historic Site',
'Golden Gate National Recreation Area',
'Golden Spike National Historical Park',
'Governors Island National Monument',
'Grand Canyon National Park',
'Grand Portage National Monument',
'Grand Teton National Park',
'Grant-Kohrs Ranch National Historic Site',
'Great Basin National Park',
'Great Egg Harbor River',
'Great Falls Park',
'Great Sand Dunes National Park & Preserve',
'Great Smoky Mountains National Park',
'Green Springs',
'Greenbelt Park',
'Guadalupe Mountains National Park',
'Guilford Courthouse National Military Park',
'Gulf Islands National Seashore',
'Gullah/Geechee Cultural Heritage Corridor',
'Hagerman Fossil Beds National Monument',
'Haleakal&#257; National Park',
'Hamilton Grange National Memorial',
'Hampton National Historic Site',
'Harmony Hall',
'Harpers Ferry National Historical Park',
'Harriet Tubman National Historical Park',
'Harriet Tubman Underground Railroad National Historical Park',
'Harry S Truman National Historic Site',
'Hawai\'i Volcanoes National Park',
'Herbert Hoover National Historic Site',
'Historic Jamestowne Part of Colonial National Historical Park',
'Hohokam Pima National Monument',
'Home Of Franklin D Roosevelt National Historic Site',
'Homestead National Monument of America',
'Honouliuli National Historic Site',
'Hopewell Culture National Historical Park',
'Hopewell Furnace National Historic Site',
'Horseshoe Bend National Military Park',
'Hot Springs National Park',
'Hovenweep National Monument',
'Hubbell Trading Post National Historic Site',
'Hudson River Valley National Heritage Area',
'I&#241;upiat Heritage Center',
'Ice Age Floods National Geologic Trail',
'Ice Age National Scenic Trail',
'Independence National Historical Park',
'Indiana Dunes National Park',
'Isle Royale National Park',
'James A Garfield National Historic Site',
'Jean Lafitte National Historical Park and Preserve',
'Jewel Cave National Monument',
'Jimmy Carter National Historic Site',
'John Day Fossil Beds National Monument',
'John Fitzgerald Kennedy National Historic Site',
'John H. Chafee Blackstone River Valley National Heritage Corridor',
'John Muir National Historic Site',
'Johnstown Flood National Memorial',
'Joshua Tree National Park',
'Journey Through Hallowed Ground National Heritage Area',
'Juan Bautista de Anza National Historic Trail',
'Kalaupapa National Historical Park',
'Kaloko-Honok&#333;hau National Historical Park',
'Katahdin Woods and Waters National Monument',
'Katmai National Park & Preserve',
'Kenai Fjords National Park',
'Kenilworth Park & Aquatic Gardens',
'Kennesaw Mountain National Battlefield Park',
'Keweenaw National Historical Park',
'Kings Mountain National Military Park',
'Klondike Gold Rush - Seattle Unit National Historical Park',
'Klondike Gold Rush National Historical Park',
'Knife River Indian Villages National Historic Site',
'Kobuk Valley National Park',
'Korean War Veterans Memorial',
'Lake Clark National Park & Preserve',
'Lake Mead National Recreation Area',
'Lake Meredith National Recreation Area',
'Lake Roosevelt National Recreation Area',
'Lassen Volcanic National Park',
'Lava Beds National Monument',
'LBJ Memorial Grove on the Potomac',
'Lewis & Clark National Historic Trail',
'Lewis and Clark National Historical Park',
'Lincoln Boyhood National Memorial',
'Lincoln Home National Historic Site',
'Lincoln Memorial',
'Little Bighorn Battlefield National Monument',
'Little River Canyon National Preserve',
'Little Rock Central High School National Historic Site',
'Longfellow House Washington\'s Headquarters National Historic Site',
'Lowell National Historical Park',
'Lower Delaware National Wild and Scenic River',
'Lower East Side Tenement Museum National Historic Site',
'Lyndon B Johnson National Historical Park',
'Maggie L Walker National Historic Site',
'Maine Acadian Culture',
'Mammoth Cave National Park',
'Manassas National Battlefield Park',
'Manhattan Project National Historical Park',
'Manzanar National Historic Site',
'Marsh - Billings - Rockefeller National Historical Park',
'Martin Luther King, Jr. Memorial',
'Martin Luther King, Jr. National Historical Park',
'Martin Van Buren National Historic Site',
'Mary McLeod Bethune Council House National Historic Site',
'Mesa Verde National Park',
'Minidoka National Historic Site',
'Minute Man National Historical Park',
'Minuteman Missile National Historic Site',
'Mississippi Delta National Heritage Area',
'Mississippi Gulf National Heritage Area',
'Mississippi Hills National Heritage Area',
'Mississippi National River and Recreation Area',
'Missouri National Recreational River',
'Mojave National Preserve',
'Monocacy National Battlefield',
'Montezuma Castle National Monument',
'Moores Creek National Battlefield',
'Mormon Pioneer National Historic Trail',
'Morristown National Historical Park',
'Motor Cities National Heritage Area',
'Mount Rainier National Park',
'Mount Rushmore National Memorial',
'Muir Woods National Monument',
'Muscle Shoals National Heritage Area',
'Natchez National Historical Park',
'Natchez Trace National Scenic Trail',
'Natchez Trace Parkway',
'National Aviation Heritage Area',
'National Capital Parks-East',
'National Mall and Memorial Parks',
'National Park of American Samoa',
'National Parks of New York Harbor',
'Natural Bridges National Monument',
'Navajo National Monument',
'New Bedford Whaling National Historical Park',
'New England National Scenic Trail',
'New Jersey Pinelands National Reserve',
'New Orleans Ja\' National Historical Park',
'New River Gorge National River',
'Nez Perce National Historical Park',
'Niagara Falls National Heritage Area',
'Nicodemus National Historic Site',
'Ninety Six National Historic Site',
'Niobrara National Scenic River',
'Noatak National Preserve',
'North Cascades National Park',
'North Country National Scenic Trail',
'Obed Wild & Scenic River',
'Ocmulgee Mounds National Historical Park',
'Oil Region National Heritage Area',
'Oklahoma City National Memorial',
'Old Spanish National Historic Trail',
'Olympic National Park',
'Oregon Caves National Monument & Preserve',
'Oregon National Historic Trail',
'Organ Pipe Cactus National Monument',
'Overmountain Victory National Historic Trail',
'Oxon Cove Park & Oxon Hill Farm',
'Ozark National Scenic Riverways',
'Padre Island National Seashore',
'Palo Alto Battlefield National Historical Park',
'Parashant National Monument',
'Paterson Great Falls National Historical Park',
'Pea Ridge National Military Park',
'Pearl Harbor National Memorial',
'Pecos National Historical Park',
'Pennsylvania Avenue',
'Perry\'s Victory & International Peace Memorial',
'Petersburg National Battlefield',
'Petrified Forest National Park',
'Petroglyph National Monument',
'Pictured Rocks National Lakeshore',
'Pinnacles National Park',
'Pipe Spring National Monument',
'Pipestone National Monument',
'Piscataway Park',
'Point Reyes National Seashore',
'Pony Express National Historic Trail',
'Port Chicago Naval Magazine National Memorial',
'Potomac Heritage National Scenic Trail',
'Poverty Point National Monument',
'President William Jefferson Clinton Birthplace Home National Historic Site',
'President\'s Park (White House)',
'Presidio of San Francisco',
'Prince William Forest Park',
'Pu`uhonua O H&#333;naunau National Historical Park',
'Pu`ukohol&#257; Heiau National Historic Site',
'Pullman National Monument',
'Rainbow Bridge National Monument',
'Reconstruction Era National Historical Park',
'Redwood National and State Parks',
'Richmond National Battlefield Park',
'Rio Grande Wild & Scenic River',
'River Raisin National Battlefield Park',
'Rivers Of Steel National Heritage Area',
'Rock Creek Park',
'Rocky Mountain National Park',
'Roger Williams National Memorial',
'Roosevelt Campobello International Park',
'Rosie the Riveter WWII Home Front National Historical Park',
'Russell Cave National Monument',
'Sagamore Hill National Historic Site',
'Saguaro National Park',
'Saint Croix Island International Historic Site',
'Saint Croix National Scenic Riverway',
'Saint Paul\'s Church National Historic Site',
'Saint-Gaudens National Historical Park',
'Salem Maritime National Historic Site',
'Salinas Pueblo Missions National Monument',
'Salt River Bay National Historical Park and Ecological Preserve',
'San Antonio Missions National Historical Park',
'San Francisco Maritime National Historical Park',
'San Juan Island National Historical Park',
'San Juan National Historic Site',
'Sand Creek Massacre National Historic Site',
'Santa Fe National Historic Trail',
'Santa Monica Mountains National Recreation Area',
'Saratoga National Historical Park',
'Saugus Iron Works National Historic Site',
'Schuylkill River Valley National Heritage Area',
'Scotts Bluff National Monument',
'Selma To Montgomery National Historic Trail',
'Sequoia & Kings Canyon National Parks',
'Shenandoah National Park',
'Shenandoah Valley Battlefields National Historic District',
'Shiloh National Military Park',
'Sitka National Historical Park',
'Sleeping Bear Dunes National Lakeshore',
'South Carolina National Heritage Corridor',
'Springfield Armory National Historic Site',
'Star-Spangled Banner National Historic Trail',
'Statue Of Liberty National Monument',
'Steamtown National Historic Site',
'Stones River National Battlefield',
'Stonewall National Monument',
'Sunset Crater Volcano National Monument',
'Tallgrass Prairie National Preserve',
'Tennessee Civil War National Heritage Area',
'Thaddeus Kosciuszko National Memorial',
'The Last Green Valley National Heritage Corridor',
'Theodore Roosevelt Birthplace National Historic Site',
'Theodore Roosevelt Inaugural National Historic Site',
'Theodore Roosevelt Island',
'Theodore Roosevelt National Park',
'Thomas Cole National Historic Site',
'Thomas Edison National Historical Park',
'Thomas Jefferson Memorial',
'Thomas Stone National Historic Site',
'Timpanogos Cave National Monument',
'Timucuan Ecological & Historic Preserve',
'Tonto National Monument',
'Touro Synagogue National Historic Site',
'Trail Of Tears National Historic Trail',
'Tule Lake National Monument',
'Tule Springs Fossil Beds National Monument',
'Tumacácori National Historical Park',
'Tupelo National Battlefield',
'Tuskegee Airmen National Historic Site',
'Tuskegee Institute National Historic Site',
'Tuzigoot National Monument',
'Ulysses S Grant National Historic Site',
'Upper Delaware Scenic & Recreational River',
'Valles Caldera National Preserve',
'Valley Forge National Historical Park',
'Vanderbilt Mansion National Historic Site',
'Vicksburg National Military Park',
'Vietnam Veterans Memorial',
'Virgin Islands Coral Reef National Monument',
'Virgin Islands National Park',
'Voyageurs National Park',
'Waco Mammoth National Monument',
'Walnut Canyon National Monument',
'War In The Pacific National Historical Park',
'Washington Monument',
'Washington-Rochambeau National Historic Trail',
'Washita Battlefield National Historic Site',
'Weir Farm National Historic Site',
'Wheeling National Heritage Area',
'Whiskeytown National Recreation Area',
'White Sands National Monument',
'Whitman Mission National Historic Site',
'William Howard Taft National Historic Site',
'Wilson\'s Creek National Battlefield',
'Wind Cave National Park',
'Wing Luke Museum Affiliated Area',
'Wolf Trap National Park for the Performing Arts',
'Women\'s Rights National Historical Park',
'World War II Memorial',
'Wrangell - St Elias National Park & Preserve',
'Wright Brothers National Memorial',
'Wupatki National Monument',
'Yellowstone National Park',
'Yorktown Battlefield Part of Colonial National Historical Park',
'Yosemite National Park',
'Yucca House National Monument',
'Yukon - Charley Rivers National Preserve'
]

states = states = {'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}

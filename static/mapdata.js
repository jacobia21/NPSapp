var simplemaps_usmap_mapdata={
  main_settings: {
   //General settings
    width: screen.width * .75, //'700' or 'responsive'
    background_color: "#FFFFFF",
    background_transparent: "yes",

    //Label defaults
    label_color: "#002767",
    hide_labels: "no",
    border_color: "white",

    //State defaults
    state_description: "See the parks in this state",
    state_color: "silver",
    state_hover_color: "gold",
    state_url: "",
    all_states_inactive: "no",

    //Zoom settings
    zoom: "yes",
    initial_zoom: "-1",
    initial_zoom_solo: "yes",

    //Advanced settings
    div: "map",
    state_image_url: "",
    state_image_position: "",
    location_image_url: "",
    label_hover_color: "",
    label_size: "",
    label_font: "",
    popups: "detect"
  },
  state_specific: {
    HI: {
      name: "Hawaii",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"hi\""
    },
    AK: {
      name: "Alaska",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ak\""
    },
    FL: {
      name: "Florida",
      inactive: "no",
      hide: "no",
      url:"http://localhost:5000/parks_by_state/\"fl\""
    },
    NH: {
      name: "New Hampshire",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"nh\""
    },
    VT: {
      name: "Vermont",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"vt\""
    },
    ME: {
      name: "Maine",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"me\""
    },
    RI: {
      name: "Rhode Island",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ri\""
    },
    NY: {
      name: "New York",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ny\""
    },
    PA: {
      name: "Pennsylvania",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"pa\""
    },
    NJ: {
      name: "New Jersey",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"nj\""
    },
    DE: {
      name: "Delaware",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"de\""
    },
    MD: {
      name: "Maryland",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"md\""
    },
    VA: {
      name: "Virginia",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"va\""
    },
    WV: {
      name: "West Virginia",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"wv\""
    },
    OH: {
      name: "Ohio",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"oh\""
    },
    IN: {
      name: "Indiana",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"in\""
    },
    IL: {
      name: "Illinois",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"il\""
    },
    CT: {
      name: "Connecticut",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ct\""
    },
    WI: {
      name: "Wisconsin",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"wi\""
    },
    NC: {
      name: "North Carolina",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"nc\""
    },
    DC: {
      name: "District of Columbia",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"dc\""
    },
    MA: {
      name: "Massachusetts",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ma\""
    },
    TN: {
      name: "Tennessee",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"tn\""
    },
    AR: {
      name: "Arkansas",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ar\""
    },
    MO: {
      name: "Missouri",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"mo\""
    },
    GA: {
      name: "Georgia",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ga\""
    },
    SC: {
      name: "South Carolina",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"sc\""
    },
    KY: {
      name: "Kentucky",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ky\""
    },
    AL: {
      name: "Alabama",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"al\""
    },
    LA: {
      name: "Louisiana",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"la\""
    },
    MS: {
      name: "Mississippi",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ms\""
    },
    IA: {
      name: "Iowa",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ia\""
    },
    MN: {
      name: "Minnesota",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"mn\""
    },
    OK: {
      name: "Oklahoma",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ok\""
    },
    TX: {
      name: "Texas",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"tx\""
    },
    NM: {
      name: "New Mexico",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"nm\""
    },
    KS: {
      name: "Kansas",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ks\""
    },
    NE: {
      name: "Nebraska",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ne\""
    },
    SD: {
      name: "South Dakota",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"sd\""
    },
    ND: {
      name: "North Dakota",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"nd\""
    },
    WY: {
      name: "Wyoming",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"wy\""
    },
    MT: {
      name: "Montana",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"mt\""
    },
    CO: {
      name: "Colorado",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"co\""
    },
    UT: {
      name: "Utah",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ut\""
    },
    AZ: {
      name: "Arizona",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"az\""
    },
    NV: {
      name: "Nevada",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"nv\""
    },
    OR: {
      name: "Oregon",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"or\""
    },
    WA: {
      name: "Washington",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"wa\""
    },
    CA: {
      name: "California",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"ca\""
    },
    MI: {
      name: "Michigan",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"mi\""
    },
    ID: {
      name: "Idaho",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"id\""
    },
    GU: {
      name: "Guam",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"gu\""
    },
    VI: {
      name: "Virgin Islands",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"vi\""
    },
    PR: {
      name: "Puerto Rico",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"pr\""
    },
    MP: {
      name: "Northern Mariana Islands",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"mp\""
    },
    AS: {
      name: "American Samoa",
      hide: "no",
      inactive: "no",
      url:"http://localhost:5000/parks_by_state/\"as\""
    }
  }
};

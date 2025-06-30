import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'geopotential', 'relative_humidity', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
        ],
        'pressure_level': [
            '50', '500', '850',
            '1000',
        ],
        'year': '2020',
        'month': '08',
        'day': [
            '26',
        ],
        'time': [
            '00:00',
        ],
    },
    '20200826_20200830_pl.nc')

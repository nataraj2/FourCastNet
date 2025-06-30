import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature',
            'mean_sea_level_pressure', 'surface_pressure', 'total_column_water_vapour',
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
    '20200826_20200830_sfc.nc')


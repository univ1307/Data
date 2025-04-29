from xbbg import blp

#take HSI snap
def take_HSI_snap():
    try:
        response = blp.bdp("HSI Index", flds=['Last Price'])
        return response.iloc[0,0]
    except Exception as e:
        print(f'Error: {e}. Retrieving last price from internal database')
        return 0

import speedtest as st

def speed_test():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print(f'Velocidade de download em mbps: {down_speed}')

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print(f'Velocidade de upload em mbps: {up_speed}')

    ping = test.results.ping
    print(f'Ping: {ping}')

speed_test()
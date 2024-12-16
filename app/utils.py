import speedtest
import logging

def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        logging.info(f"Speed test successful: {download_speed:.2f} Mbps, {upload_speed:.2f} Mbps, Ping: {ping:.2f} ms")
        return download_speed, upload_speed, ping
    except Exception as e:
        logging.error(f"Error during internet speed test: {e}")
        return None, None, None

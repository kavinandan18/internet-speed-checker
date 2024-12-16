HEADER_STYLE = """
<h1 style='text-align: center; color: #4CAF50;'>Internet Speed Checker</h1>
"""

RESULT_BOX_STYLE = """
<div style='border: 2px solid #4CAF50; border-radius: 10px; padding: 20px; background-color: #E8F5E9;'>
    <h3>Results:</h3>
    <p><strong>Download Speed:</strong> {download_speed:.2f} Mbps</p>
    <p><strong>Upload Speed:</strong> {upload_speed:.2f} Mbps</p>
    <p><strong>Ping:</strong> {ping:.2f} ms</p>
</div>
"""

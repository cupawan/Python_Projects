from DatetimeUtils import CommonUtils

class Formatter:
    def __init__(self):
        pass
    
    def formatBasicWeatherReportEmail(name, location, vals):
        weather_report = f"""
                            <html>
                            <head>
                                <style>
                                    body {{
                                        font-family: 'Arial', sans-serif;
                                        background-color: #eff8ff;
                                        color: #333;
                                        margin: 20px;
                                    }}
                                    .report-container {{
                                        max-width: 600px;
                                        margin: 0 auto;
                                        padding: 20px;
                                        border: 2px solid #3498db;
                                        border-radius: 10px;
                                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                        background-color: #fff;
                                    }}
                                    .highlight {{
                                        color: #e74c3c;
                                        font-weight: bold;
                                    }}
                                    .important {{
                                        background-color: #f8d7da;
                                        padding: 2px;
                                        color: #721c24;
                                        border-radius: 3px;
                                    }}
                                </style>
                            </head>
                            <body>

                            <div class="report-container">
                                <h2>Weather Report</h2>
                                <h3>Good Morning, {name}</h3>

                                <p>
                                    The current weather report for <span class="highlight">{vals[0]}</span> at  <span class="highlight">{location}</span> is as follows:
                                </p>

                                <p>
                                    <strong>Sunrise:</strong> {vals[1]} | <strong>Sunset:</strong> {vals[2]}
                                </p>

                                <p>
                                    The temperature is <span class="highlight">{vals[3]}</span>, and it feels like <span class="highlight">{vals[4]}</span>. The atmospheric pressure is <span class="highlight">{vals[5]}</span>,
                                    humidity is <span class="highlight">{vals[6]}</span>, and the dew point is <span class="highlight">{vals[7]}</span>.
                                </p>

                                <p>
                                    The UV Index is <span class="highlight">{vals[8]}</span>, clouds cover <span class="highlight">{vals[9]}</span> of the sky, and visibility is <span class="highlight">{vals[10]}</span>.
                                </p>

                                <p>
                                    Wind speed is <span class="highlight">{vals[11]}</span>, coming from <span class="highlight">{vals[12]}</span> degrees.
                                </p>
                                <p> Have a nice day! </p>
                            </div>

                            </body>
                            </html>
                            """
 
        return weather_report

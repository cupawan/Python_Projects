from EmailUtils import SendEmail
from OWMScript import OpenWeatherMap
from FormattingUtils import Formatter


if __name__ == "__main__":
    contacts = {'username@gmail.com' :[('latitude_value', 'longitude_value'),'Location','Name']}
    try:
        owm = OpenWeatherMap()
        email_instance = SendEmail(is_html = True)
        formatter = Formatter()
        for rec_mail, (coords, location, n) in contacts.items():
            latitude, longitude = coords
            v = owm.request_weather_data(lat=latitude, lon=longitude)
            email_body = formatter.formatBasicWeatherReportEmail(location=location, vals=v)
            email_instance.send_email(send_to=rec_mail, subject=f"Weather Email", email_body=email_body)
            print(f"Email Sent to {n}")
    except Exception as e:
        raise
    
    
    

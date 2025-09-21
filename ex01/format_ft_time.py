import datetime as dt

now = dt.datetime.now()
epoch_seconds = now.timestamp()
thousand_format = "{:,}".format(epoch_seconds)
scientific_format = "{:.2e}".format(epoch_seconds)

print(f"Seconds since January 1, 1970: {thousand_format} or {scientific_format} in scientific notation")
print(now.strftime("%b %d %Y"))
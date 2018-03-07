# amzn-dash-hack
dash-buttonｗお

## Please make "_settings.json" in the working directly.

```json:_settings.json
{
    "dash_button": {
        "macaddress": [
            "XX:XX:XX:XX:XX:XX"
        ]
    }
}
```

"XX:XX:XX:XX:XX:XX" is your amazon dash button macaddress.
If you add macaddress, please write the address by reference to 👇

```json:_settings.json
{
    "dash_button": {
        "macaddress": [
            "XX:XX:XX:XX:XX:XX",
            "XX:XX:XX:XX:XX:XX",
            "XX:XX:XX:XX:XX:XX"
        ]
    }
}
```

## Run dash-hook.py with sudo.


```shellscript:shell.sh
sudo python3 dash-hook.py
```

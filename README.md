BrowserStack Screenshot API Wrapper
=========
This is a wrapper for BrowserStack Screenshot API, implemented in python. 
###Usage
--------------------
import screenshot

###Creating Client
-------------------
Creates a new client instance.

  * `username`: The username for the BrowserStack account.
  * `password`: The password for the BrowserStack account.

``` python
username = "name@example.com"
password = "pwd"
obj = Screenshot(username, password)
```

###Methods
------------------
* `get_os_browsers` - returns the list of all OS and Browsers supported by BrowserStack in json format

* `get_screenshot(**params)` - takes the screenshots
set params={...} and call the function as get_screenshots(**params)
####Example
Eg setting object:
``` python
params = {
	url = "www.google.com",
	callback_url = "http://example.com/pingback_url",
	win_res = "1024x768",		#Options : "1024x768", "1280x1024"
	mac_res = "1920x1080", 	#Options : "1024x768", "1280x960", "1280x1024", "1600x1200", "1920x1080"
	quality = "compressed",	#Options : "compressed", "original"
	wait_time = 5,          	#Options: 2, 5, 10, 15, 20, 60
	orientation = "portrait", #Options: "portrait", "landscape"
	tunnel = false,
	browsers = [
			{os="Windows", os_version="7", browser="ie", browser_version="8.0"},
			{os="Windows", os_version="XP", browser="ie", browser_version="7.0"}
	]
}
```
* `get_full_status` - gives the list of screenshots and their states in json format

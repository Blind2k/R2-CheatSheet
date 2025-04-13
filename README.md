[//]: <> (Welcome! I like how you think!)
```text
     `7MM"""Mq.                     .g8"""bgd  .M"""bgd  
       MM   `MM.                  .dP'     `M ,MI    "Y
       MM   ,M9     pd*"*b.       dM'       ` `MMb.    
       MMmmdM9     (O)   j8  ==== MM            `YMMNq.
       MM  YM.         ,;j9       MM.         .     `MM
       MM   `Mb.    ,-='          `Mb.     ,' Mb     dM
     .JMML.  .JMM. .Ammmmmmm        '"cheat"   "sheet"   

              Your Interactive Cheat Sheet
```
# R2-CheatSheet
A command-line (CLI) tool for Penetration Test (PT), CTF, or Bug Bounty.  
Designed to speed up common attack workflows with copy-paste commands. Configure the IP, AD, or creds and get the commands ready for execution.

### Advantages
**Chain Commands:** Run many commands in one line using `;`  
**Aliases Friendly:** First 2 letters are an alias. `lh` for `lhost`.  
**Full Personalization:** Add aliases in [english_strings.py](app_data/en/english_strings.py)  
**Smart Parsing:** Case does not matter — `SEt`, `set`, or `SET` all work  
**Modern Python:** Designed for Python 3.10+

## Example
> python3 r2cs.py  
> set rhost 192.168.1.50; se rp 9999  
> 2; 2  

###### Output
> Netcat: Target  
> nc 192.168.1.50 9999

# Beginners Friendly
## Easy installation
Simply copy-paste to your Linux terminal.  
The script will ensure Python is above 3.10. After that, Install Git and Terminator 
> curl -L https://github.com/Blind2k/R2-CheatSheet/raw/refs/heads/main/app_data/installation-scripts/install_r2-cs.bash | bash

## Video instruction
Watch the video to learn more.
---

### Steps 
`1.` Choose environment: OS, Service, or Protocol-specific  
`2.` Set variables: LHOST, LPORT, RPORT...  
`3.` Copy-paste the command in the Terminal  
`4.` Run & Repeat  

## Step `1`: Choose environment
| Category     | Subcategories                                                                                                                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Linux**    | 1. Chained Commands  <br> 2. General Commands  <br> 3. Privilege Escalation                                                                                                                                         |
| **Windows**  | 1. PowerShell Chained Commands  <br> 2. General Commands  <br> 3. Privilege Escalation  <br> 4. Command Prompt  <br> 5. Active Directory  <br> 6. Defence Services                                                  |
| **Protocols**| 1. Day Time  <br> 2. FTP  <br> 3. SSH  <br> 4. Telnet  <br> 5. SMTP  <br> 6. DNS  <br> 7. DHCP  <br> 8. POP3  <br> 9. IMAP  <br> 10. SMB  <br> 11. SNMP  <br> 12. HTTP  <br> 13. HTTPS  <br> 14. RDP  <br> 15. FTPS |
| **Databases**| 1. MySQL  <br> 2. PostgreSQL  <br> 3. GraphQL                                                                                                                                                                       |
| **AWS**      | 1. S3  <br> 2. IAM  <br> 3. Lambda  <br> 4. API Gateway  <br> 5. EC2  <br> 6. SSM  <br> 7. Configurations  <br> 8. Misc                                                                                             |

## Step `2`: Configure Variables
### Configuration Operators — What?
```text
set,    se  <option> <value> Define a variable
unset,  un  <option>         Reset variable
get         <option>         -To be developed-
run                          -To be developed-
```
### Configuration Keys — Which?
#### 1. Local Options:
```text
lhost,   lh         Your IP/domain to work with
lport,   lp         Your local port number
proxy,   pr         Optional proxy (http://ip:port)
awsuser, awsu       AWS profile username
```
#### 2. Target Options:
```text
rhost,  rh          Target host IP or domain
rport,  rp          Target port
domain, AD          Active Directory/forest domain
path,   uri         File or path on RHost
```
#### 3. Authentication:
```text
username, us, user  Single username
password, pa, pw    Single password
```
#### 4. Wordlists:
```text
usernames, uf       File containing usernames
passwords, pf       File containing passwords
wordlist,  wl       Generic wordlist (e.g., for paths)
```
## Navigation Commands
```text
  help, he, ?, ah?          Show help message
  menu, me                  Print current options
  back, ba, up, main        Go back one menu level
  quit, qu, exit, bye       Exit the tool
```

Feel free to [Contact Me](mailto:buggedsystem+R2CS@gmail.com)
# P.S.
I'm searching for a Junior PT position.  
Every bone in my body will be grateful for an opportunity.
Furthermore, I will be super happy for ideas, offers, or just pictures of dogs... Yeah VX, I'm looking at U!.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-alpha-orange)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

# Technical Information
## Test strings
<pre>
# Set Test
set rhost 8.8.8.8;set rport 838; set nic eth0; set domain slam.com;set path /home/user/you/; set username SLAME@!#@!;set password SLAMDUNK_PASSWORD;set usernames app_data/wordlists/wordlist_test.txt;set passwords app_data/wordlists/wordlist_test.txt;set wordlist app_data/wordlists/wordlist_test.txt;set lhost 1.1.1.1;set lport 3838
</pre>
<pre>
# Unset Test
unset rhost; unset rport;unset domain ;unset path ;unset username ;unset password; unset usernames;unset passwords ;unset wordlist ;unset lhost;unset lport
</pre>
## Class Configuration
| Local Host  | Remote Host |           Description |
|-------------|:-----------:|----------------------:|
| lhost       |    rhost    |        IP/domain/host |
| lport       |    rport    |        Port (0-65535) |
| proxy       |      -      |                String |
| aws profile |      -      |                String |
| NIC         |      -      |                String |
| -           |   domain    |                String |
| -           |    path     |                String |
| -           |  username   |                String |
| -           |  password   |                String |
| -           |  usernames  | Path & not empty File |
| -           |  passwords  | Path & not empty File |
| -           |  wordlist   | Path & not empty File |


## Future Ideas
- [ ] Create process to run the commands
- [ ] Allow attacking multiple domains or IPs
- [ ] Create a class to each session
- [ ] Create classes for AWS, Brute-Force Session
- [ ] Tab completion
- [ ] History


Please, do not use this tool for any criminal activity. I don't take ANY responsibility for the side effects occur when using this tool and the data.

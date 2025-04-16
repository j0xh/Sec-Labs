\ Well-Known Ports (0-1023)

| Port Number | Protocol     | Description                                               |
|-------------|--------------|-----------------------------------------------------------|
| 20, 21      | FTP          | File Transfer Protocol - Used for transferring files      |
| 22          | SSH          | Secure Shell - Secure remote access to a server           |
| 23          | Telnet       | Telnet - Unencrypted remote terminal access              |
| 25          | SMTP         | Simple Mail Transfer Protocol - Sending emails           |
| 53          | DNS          | Domain Name System - Resolves domain names to IPs         |
| 67, 68      | DHCP         | Dynamic Host Configuration Protocol - Assigns IPs         |
| 80          | HTTP         | HyperText Transfer Protocol - Unencrypted web traffic     |
| 110         | POP3         | Post Office Protocol 3 - Retrieves emails from a server  |
| 143         | IMAP         | Internet Message Access Protocol - Email retrieval        |
| 443         | HTTPS        | HyperText Transfer Protocol Secure - Encrypted web traffic|
| 3389        | RDP          | Remote Desktop Protocol - Remote GUI-based desktop access |

---

\ Common Security Ports

| Port Number | Protocol     | Description                                               |
|-------------|--------------|-----------------------------------------------------------|
| 389         | LDAP         | Lightweight Directory Access Protocol - Access directory services |
| 636         | LDAPS        | LDAP Secure - Secure version of LDAP                      |
| 443         | HTTPS        | HTTP Secure - Secure version of HTTP, uses TLS/SSL         |
| 993         | IMAPS        | IMAP Secure - Secure version of IMAP                       |
| 995         | POP3S        | POP3 Secure - Secure version of POP3                       |
| 3306        | MySQL        | MySQL Database - Open-source relational database           |
| 5432        | PostgreSQL   | PostgreSQL Database - Open-source relational database      |

---

\ Common Network Services & Protocols

| Protocol    | Port Number | Description                                               |
|-------------|-------------|-----------------------------------------------------------|
| TCP         | N/A         | Transmission Control Protocol - Connection-oriented protocol for reliable data transfer |
| UDP         | N/A         | User Datagram Protocol - Connectionless protocol for fast data transfer |
| ICMP        | N/A         | Internet Control Message Protocol - Used for diagnostic tools (e.g., ping) |
| SNMP        | 161         | Simple Network Management Protocol - Manages devices on a network |
| NTP         | 123         | Network Time Protocol - Synchronizes clocks over a network |
| SIP         | 5060        | Session Initiation Protocol - Used for initiating and controlling voice and video calls |

---

\ Other Important Ports

| Port Number | Protocol     | Description                                               |
|-------------|--------------|-----------------------------------------------------------|
| 137-139     | NetBIOS      | Network Basic Input/Output System - Provides network services like file sharing |
| 161         | SNMP         | Simple Network Management Protocol - Network device management |
| 1723        | PPTP         | Point-to-Point Tunneling Protocol - VPN protocol           |
| 3389        | RDP          | Remote Desktop Protocol - Provides GUI access to remote systems |

---

\ Tips

- TCP vs. UDP: TCP is connection-oriented and reliable, while UDP is connectionless and faster but less reliable.
- Ports below 1024 are considered well-known ports and are typically reserved for system or privileged services.
- Port 443 (HTTPS) is essential for secure communication over the web—ensure all sensitive traffic uses it!
